import datetime
import pandas
import seaborn
import statsmodels.formula.api as smf
import warnings

from sklearn import linear_model, preprocessing
from sklearn.exceptions import DataConversionWarning
from sqlalchemy import and_

from readop.database.session import Session
from readop.database.models import Operation


class LinearRegression:
    def __init__(
            self,
            access_pattern_id: int,
            storage_unit_id: int
    ):
        # ignore warning when converting database data from into to float
        warnings.filterwarnings(action='ignore', category=DataConversionWarning)

        self.data_frame = pandas.DataFrame()

        self.access_pattern_id = access_pattern_id
        self.storage_unit_id = storage_unit_id

        self.file_path = str(self.access_pattern_id) + '-'
        self.file_path += str(self.storage_unit_id) + '---'

        timestamp = str(datetime.datetime.now()).replace(' ', '-')
        timestamp = timestamp[:timestamp.find('.')]
        timestamp = timestamp.replace(':', '.')
        self.file_path += timestamp

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
                Operation.storage_unit_id == self.storage_unit_id
            )).statement,
            session.bind
        )

        session.close()

    def normalize_data(self, feature_range: tuple = (0, 100)) -> None:
        data = self.data_frame.values
        scaler = preprocessing.MinMaxScaler(feature_range=feature_range)
        data_normalized = scaler.fit_transform(data)
        self.data_frame = pandas.DataFrame(data_normalized, columns=self.data_frame.columns)

    def get_coefficients(self) -> list:
        return linear_model.LinearRegression().fit(
            self.data_frame[[
                'apd_access_seq_threshold',
                'apd_access_random_threshold',
                'apd_access_random_inc_threshold'
            ]],
            self.data_frame['total_bytes_read']
        ).coef_

    def get_summary(self) -> str:
        formula = (
            'total_bytes_read ~ '
            'apd_access_seq_threshold + '
            'apd_access_random_threshold + '
            'apd_access_random_inc_threshold'
        )

        model = smf.ols(formula=formula, data=self.data_frame).fit()

        return str(model.summary())

    def write_summary(self):
        summary = self.get_summary()
        file_path = self.file_path + '.txt'

        with open(file_path, 'w') as file:
            file.write(summary)

        return file_path

    def write_pairplot(self, file_prefix: str = '') -> str:
        x_vars = [
            'apd_access_seq_threshold',
            'apd_access_random_threshold',
            'apd_access_random_inc_threshold'
        ]

        y_vars = [
            'total_bytes_read'
        ]

        file_path = file_prefix + self.file_path + '.png'

        plot = seaborn.pairplot(self.data_frame, x_vars=x_vars, y_vars=y_vars, height=7, aspect=0.7, kind='reg')
        plot.savefig(file_path)

        return file_path
