import datetime
import pandas

from sqlalchemy import and_

from readop.analytics.linear_regression import LinearRegression
from readop.database.models.operation import Operation
from readop.database.session import Session
from readop.managers.operation import OperationManager
from readop.models.range import Range
from readop.utility.operation_generator import generate_operation_list_from_ranges


MIN_RANGE_REDUCTION_COEFFICIENT = 0.2
MAX_RANGE_REDUCTION_COEFFICIENT = 1.0

separator_0 = ('=' * 100) + '\n' + ('+' * 100) + '\n' + ('=' * 100)
separator_1 = ('-' * 100)
separator_2 = '-' * 50


def calculate_range_scale(linear_regression_coefficient: float) -> float:
    # y = 0.5 / (2x + 0.5)
    # https://www.desmos.com/calculator/vsrke1icej
    linear_regression_coefficient = abs(linear_regression_coefficient)

    range_reduction_coefficient = 0.5 / (2.0 * linear_regression_coefficient + 0.5)

    # clamp
    range_reduction_coefficient = min(range_reduction_coefficient, MAX_RANGE_REDUCTION_COEFFICIENT)
    range_reduction_coefficient = max(range_reduction_coefficient, MIN_RANGE_REDUCTION_COEFFICIENT)

    return range_reduction_coefficient


class LinearRegressionGuided(LinearRegression):
    def __init__(
            self,
            access_pattern_id: int,
            storage_unit_id: int,
            ops_per_iteration: int,
            system_description_id: int = 1
    ):
        super().__init__(access_pattern_id, storage_unit_id)

        self.operation_manager = OperationManager()

        self.ops_per_iteration = ops_per_iteration

        f = int((ops_per_iteration + 1) ** (1.0 / 3))
        self.factors = [f, f, f]
        self.ranges = [Range(0, 100), Range(0, 100), Range(0, 100)]

        self.system_description_id = system_description_id

    def execute(self, iteration_count: int) -> None:
        self.log(separator_0)
        self.log(str(datetime.datetime.now()))
        self.log('Executing {0} iterations.'.format(iteration_count))

        for i in range(iteration_count):
            self.execute_iteration(i)

        self.log(separator_1)
        self.log('Best operation overall:')
        self.log(self.get_best_operation())

    def execute_iteration(self, iteration_number: int) -> None:
        self.log(separator_1)
        self.log('Executing iteration {0}.'.format(iteration_number))
        self.log(separator_1)

        self.log(separator_2)
        self.log('Initial ranges:')
        self.log('seq:      {0}'.format(self.ranges[0]))
        self.log('rand:     {0}'.format(self.ranges[1]))
        self.log('rand_inc: {0}'.format(self.ranges[2]))

        self.log('Initial factors:')
        self.log('seq:      {0}'.format(self.factors[0]))
        self.log('rand:     {0}'.format(self.factors[1]))
        self.log('rand_inc: {0}'.format(self.factors[2]))

        # generate and execute ops based on ranges and factors
        operations = generate_operation_list_from_ranges(
            self.ranges,
            self.factors,
            self.access_pattern_id,
            self.storage_unit_id,
            self.system_description_id
        )
        self.log(separator_2)
        self.log('Executing {0} operations:'.format(len(operations)))
        for op in operations:
            self.operation_manager.execute_operation(op)
            self.log(op)

        # linear regression analysis
        self.load_data_frame()
        # use normalized data
        self.normalize_data()
        coefs = self.get_coefficients()
        self.log(separator_2)
        self.log('linear regression coefficients:')
        self.log('[{0}, {1}, {2}]'.format(coefs[0], coefs[1], coefs[2]))
        # log summary
        self.log(self.get_summary())
        # write plot
        plot_path = self.write_pairplot(file_prefix='iteration-{0}---'.format(iteration_number))
        self.log('Pairplot written to: {0}'.format(plot_path))

        # modify ranges and factors
        self.adjust_ranges(coefs)
        self.adjust_factors(coefs)

        self.log(separator_2)
        self.log('adjusted ranges:')
        self.log('seq:      {0}'.format(self.ranges[0]))
        self.log('rand:     {0}'.format(self.ranges[1]))
        self.log('rand_inc: {0}'.format(self.ranges[2]))

        self.log('adjusted factors:')
        self.log('seq:      {0}'.format(self.factors[0]))
        self.log('rand:     {0}'.format(self.factors[1]))
        self.log('rand_inc: {0}'.format(self.factors[2]))

        self.log(separator_2)
        self.log('Best operation so far:')
        self.log(self.get_best_operation())

    def load_data_frame(self) -> None:
        session = Session()

        self.data_frame = pandas.read_sql(
            session.query(
                Operation.apd_access_seq_threshold,
                Operation.apd_access_random_threshold,
                Operation.apd_access_random_inc_threshold,
                Operation.total_bytes_read
            ).filter(and_(
                Operation.access_pattern_id == self.access_pattern_id,
                Operation.storage_unit_id == self.storage_unit_id,
                Operation.apd_access_seq_threshold >= int(self.ranges[0].min_value),
                Operation.apd_access_seq_threshold <= int(self.ranges[0].max_value),
                Operation.apd_access_random_threshold >= int(self.ranges[1].min_value),
                Operation.apd_access_random_threshold <= int(self.ranges[1].max_value),
                Operation.apd_access_random_inc_threshold >= int(self.ranges[2].min_value),
                Operation.apd_access_random_inc_threshold <= int(self.ranges[2].max_value)
            )).statement,
            session.bind
        )

        session.close()

    def adjust_ranges(self, coefs: list) -> None:
        for i in range(len(coefs)):
            self.ranges[i].scale(calculate_range_scale(coefs[i]), coefs[i] < 0)

    def adjust_factors(self, coefs: list) -> None:
        o = self.ops_per_iteration

        a = abs(coefs[0]) or 0.1
        b = abs(coefs[1]) or 0.1
        c = abs(coefs[2]) or 0.1

        x = ((a**2 * o) / (b * c))**(1/3)
        y = (b * x) / a
        z = (c * x) / a

        self.factors = [
            int(x) or 1,
            int(y) or 1,
            int(z) or 1
        ]

    def log(self, message: str) -> None:
        message = str(message)
        with open(self.file_path + '.log', 'a') as file:
            file.write(message + '\n')
        print(message)

    def get_best_operation(self) -> Operation:
        session = Session()
        operation = session.query(Operation)\
            .filter(and_(
                Operation.access_pattern_id == self.access_pattern_id,
                Operation.storage_unit_id == self.storage_unit_id
            )).order_by(Operation.total_bytes_read.asc()).first()
        session.close()
        return operation


if __name__ == '__main__':
    lrg = LinearRegressionGuided(
        access_pattern_id=6,
        storage_unit_id=1,
        ops_per_iteration=10
    )
    lrg.execute(3)
