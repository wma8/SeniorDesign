import click

from .database import DatabaseShell
from .subshell import SubShell

from readop.analytics.linear_regression import LinearRegression
from readop.analytics.linear_regression_guided import LinearRegressionGuided


class AnalyticsShell(SubShell):
    intro = \
        SubShell.separator +\
        'ReadOp Analytics subsystem.\n' + \
        SubShell.instruction_for_help + \
        SubShell.separator

    prompt = 'readop analytics > '

    def __init__(self):
        super().__init__()
        self.database_shell = DatabaseShell()

    def do_report(self, user_input):
        access_pattern = self.database_shell.choose_access_pattern()
        storage_unit = self.database_shell.choose_storage_unit()

        linear_regression = LinearRegression(access_pattern.id, storage_unit.id)
        linear_regression.load_data_frame()
        linear_regression.normalize_data()
        output_file_path = linear_regression.write_summary()

        print('Summary written to: {0}'.format(output_file_path))

    def help_report(self):
        print('Generates a Linear Regression summary.')

    def do_plot(self, user_input):
        access_pattern = self.database_shell.choose_access_pattern()
        storage_unit = self.database_shell.choose_storage_unit()

        lr = LinearRegression(access_pattern.id, storage_unit.id)
        lr.load_data_frame()
        lr.normalize_data()
        output_file_path = lr.write_pairplot()

        print('Plot written to: {0}'.format(output_file_path))

    def help_plot(self):
        print('Plots the three APD thresholds against Total Bytes Read.')

    def do_guided(self, user_input):
        access_pattern = self.database_shell.choose_access_pattern()
        storage_unit = self.database_shell.choose_storage_unit()

        iteration_count = click.prompt('Enter the number of iterations to execute', type=int)
        ops_per_iteration = click.prompt('Enter the number of operations per iteration.', type=int)

        lrg = LinearRegressionGuided(
            access_pattern.id,
            storage_unit.id,
            ops_per_iteration
        )
        lrg.execute(iteration_count)

    def help_guided(self):
        print('Executes Guided Linear Regression and generates reports.')
