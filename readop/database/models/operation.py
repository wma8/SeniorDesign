from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base import Base

from .access_pattern import AccessPattern
from .storage_unit import StorageUnit
from .system_description import SystemDescription

from readop.models.parameters import Parameters
from readop.models.results import Results
from readop.utility.validator import validate_bool, validate_int, validate_int_geq_zero


class Operation(Base):
    __tablename__ = 'operations'

    _id = Column('id', Integer, primary_key=True)
    _timestamp = Column('timestamp', DateTime(timezone=True), server_default=func.now())

    # foreign keys
    _access_pattern_id = Column('access_pattern_id', Integer, ForeignKey('access_patterns.id'), nullable=False)
    _storage_unit_id = Column('storage_unit_id', Integer, ForeignKey('storage_units.id'), nullable=False)
    _system_description_id = Column('system_description_id', Integer, ForeignKey('system_descriptions.id'), nullable=False)

    _read_ahead_enabled = Column('read_ahead_enabled', Boolean, nullable=False)

    # parameters
    _default_access_pattern = Column('default_access_pattern', Integer, nullable=False)
    _apd_data_seq_threshold = Column('apd_data_seq_threshold', Integer, nullable=False)
    _init_io_region_size = Column('init_io_region_size', Integer, nullable=False)
    _max_io_regions = Column('max_io_regions', Integer, nullable=False)
    _apd_access_seq_threshold = Column( 'apd_access_seq_threshold', Integer, nullable=False)
    _apd_access_random_threshold = Column('apd_access_random_threshold', Integer, nullable=False)
    _apd_access_random_inc_threshold = Column('apd_access_random_inc_threshold', Integer, nullable=False)

    # results
    _execution_time = Column('execution_time', Integer, nullable=False)
    _total_bytes_read = Column('total_bytes_read', BigInteger, nullable=False)
    _n_ras = Column('n_ras', BigInteger, nullable=False)
    _n_ra_cbs = Column('n_ra_cbs', BigInteger, nullable=False)
    _n_ra_out_of_seq = Column('n_ra_out_of_seq', BigInteger, nullable=False)
    _n_ra_buf_waits = Column('n_ra_buf_waits', BigInteger, nullable=False)
    _ra_buf_wait_time = Column('ra_buf_wait_time', BigInteger, nullable=False)
    _ra_data_latency = Column('ra_data_latency', BigInteger, nullable=False)
    _avg_ra_data_latency = Column('avg_ra_data_latency', BigInteger, nullable=False)
    _ddp_readext = Column('ddp_readext', BigInteger, nullable=False)

    # relationships
    _access_pattern = relationship('AccessPattern')
    _storage_unit = relationship('StorageUnit')
    _system_description = relationship('SystemDescription')

    def __init__(
            self,
            access_pattern_id: int,
            storage_unit_id: int,
            system_description_id: int,
            read_ahead_enabled: bool,
            parameters: Parameters
    ) -> None:
        self.access_pattern_id = access_pattern_id
        self.storage_unit_id = storage_unit_id
        self.system_description_id = system_description_id

        self.read_ahead_enabled = read_ahead_enabled

        self.parameters = parameters

    def __repr__(self) -> str:
        return '<Operation id={0}, seq={1}, rand={2}, rand_inc={3}, total_bytes_read={4}>'.format(
            self.id,
            self.apd_access_seq_threshold,
            self.apd_access_random_threshold,
            self.apd_access_random_inc_threshold,
            self.total_bytes_read
        )

    @hybrid_property
    def id(self) -> int:
        return self._id

    @hybrid_property
    def timestamp(self) -> DateTime:
        return self._timestamp

    @hybrid_property
    def access_pattern_id(self) -> int:
        return self._access_pattern_id

    @hybrid_property
    def storage_unit_id(self) -> int:
        return self._storage_unit_id

    @hybrid_property
    def system_description_id(self) -> int:
        return self._system_description_id

    @hybrid_property
    def access_pattern(self) -> AccessPattern:
        return self._access_pattern

    @hybrid_property
    def storage_unit(self) -> StorageUnit:
        return self._storage_unit

    @hybrid_property
    def system_description(self) -> SystemDescription:
        return self._system_description

    @hybrid_property
    def read_ahead_enabled(self) -> bool:
        return self._read_ahead_enabled

    @hybrid_property
    def default_access_pattern(self) -> int:
        return self._default_access_pattern

    @hybrid_property
    def apd_data_seq_threshold(self) -> int:
        return self._apd_data_seq_threshold

    @hybrid_property
    def init_io_region_size(self) -> int:
        return self._init_io_region_size

    @hybrid_property
    def max_io_regions(self) -> int:
        return self._max_io_regions

    @hybrid_property
    def apd_access_seq_threshold(self) -> int:
        return self._apd_access_seq_threshold

    @hybrid_property
    def apd_access_random_threshold(self) -> int:
        return self._apd_access_random_threshold

    @hybrid_property
    def apd_access_random_inc_threshold(self) -> int:
        return self._apd_access_random_inc_threshold

    @hybrid_property
    def parameters(self) -> Parameters:
        return Parameters(
            default_access_pattern=self._default_access_pattern,
            apd_data_seq_threshold=self._apd_data_seq_threshold,
            init_io_region_size=self._init_io_region_size,
            max_io_regions=self._max_io_regions,
            apd_access_seq_threshold=self._apd_access_seq_threshold,
            apd_access_random_threshold=self._apd_access_random_threshold,
            apd_access_random_inc_threshold=self._apd_access_random_inc_threshold
        )

    @hybrid_property
    def execution_time(self) -> int:
        return self._execution_time

    @hybrid_property
    def total_bytes_read(self) -> int:
        return self._total_bytes_read

    @hybrid_property
    def n_ras(self) -> int:
        return self._n_ras

    @hybrid_property
    def n_ra_cbs(self) -> int:
        return self._n_ra_cbs

    @hybrid_property
    def n_ra_out_of_seq(self) -> int:
        return self._n_ra_out_of_seq

    @hybrid_property
    def n_ra_buf_waits(self) -> int:
        return self._n_ra_buf_waits

    @hybrid_property
    def ra_buf_wait_time(self) -> int:
        return self._ra_buf_wait_time

    @hybrid_property
    def ra_data_latency(self) -> int:
        return self._ra_data_latency

    @hybrid_property
    def avg_ra_data_latency(self) -> int:
        return self._avg_ra_data_latency

    @hybrid_property
    def ddp_readext(self) -> int:
        return self._ddp_readext

    @hybrid_property
    def results(self) -> Results:
        return Results(
            execution_time=self._execution_time,
            n_ras=self._n_ras,
            n_ra_cbs=self._n_ra_cbs,
            n_ra_out_of_seq=self._n_ra_out_of_seq,
            n_ra_buf_waits=self._n_ra_buf_waits,
            ra_buf_wait_time=self._ra_buf_wait_time,
            ra_data_latency=self._ra_data_latency,
            avg_ra_data_latency=self._avg_ra_data_latency,
            ddp_readext=self._ddp_readext,
            total_bytes_read=self._total_bytes_read
        )

    @access_pattern_id.setter
    def access_pattern_id(self, access_pattern_id: int) -> None:
        self._access_pattern_id = validate_int_geq_zero(access_pattern_id)

    @storage_unit_id.setter
    def storage_unit_id(self, storage_unit_id: int) -> None:
        self._storage_unit_id = validate_int_geq_zero(storage_unit_id)

    @system_description_id.setter
    def system_description_id(self, system_description_id: int) -> None:
        self._system_description_id = validate_int_geq_zero(system_description_id)

    @read_ahead_enabled.setter
    def read_ahead_enabled(self, read_ahead_enabled: bool) -> None:
        self._read_ahead_enabled = validate_bool(read_ahead_enabled)

    @default_access_pattern.setter
    def default_access_pattern(self, default_access_pattern: int) -> None:
        self._default_access_pattern = validate_int(default_access_pattern)

    @apd_data_seq_threshold.setter
    def apd_data_seq_threshold(self, apd_data_seq_threshold: int) -> None:
        self._apd_data_seq_threshold = validate_int(apd_data_seq_threshold)

    @init_io_region_size.setter
    def init_io_region_size(self, init_io_region_size: int) -> None:
        self._init_io_region_size = validate_int(init_io_region_size)

    @max_io_regions.setter
    def max_io_regions(self, max_io_regions: int) -> None:
        self._max_io_regions = validate_int(max_io_regions)

    @apd_access_seq_threshold.setter
    def apd_access_seq_threshold(self, apd_access_seq_threshold: int) -> None:
        self._apd_access_seq_threshold = validate_int(apd_access_seq_threshold)

    @apd_access_random_threshold.setter
    def apd_access_random_threshold(self, apd_access_random_threshold: int) -> None:
        self._apd_access_random_threshold = validate_int(apd_access_random_threshold)

    @apd_access_random_inc_threshold.setter
    def apd_access_random_inc_threshold(self, apd_access_random_inc_threshold: int) -> None:
        self._apd_access_random_inc_threshold = validate_int(apd_access_random_inc_threshold)

    @parameters.setter
    def parameters(self, parameters: Parameters) -> None:
        if not isinstance(parameters, Parameters):
            raise TypeError

        self.default_access_pattern = parameters.default_access_pattern
        self.apd_data_seq_threshold = parameters.apd_data_seq_threshold
        self.init_io_region_size = parameters.init_io_region_size
        self.max_io_regions = parameters.max_io_regions
        self.apd_access_seq_threshold = parameters.apd_access_seq_threshold
        self.apd_access_random_threshold = parameters.apd_access_random_threshold
        self.apd_access_random_inc_threshold = parameters.apd_access_random_inc_threshold

    @execution_time.setter
    def execution_time(self, execution_time: int) -> None:
        self._execution_time = validate_int(execution_time)

    @total_bytes_read.setter
    def total_bytes_read(self, total_bytes_read: int) -> None:
        self._total_bytes_read = validate_int(total_bytes_read)

    @n_ras.setter
    def n_ras(self, n_ras: int) -> None:
        self._n_ras = validate_int(n_ras)

    @n_ra_cbs.setter
    def n_ra_cbs(self, n_ra_cbs: int) -> None:
        self._n_ra_cbs = validate_int(n_ra_cbs)

    @n_ra_out_of_seq.setter
    def n_ra_out_of_seq(self, n_ra_out_of_seq: int) -> None:
        self._n_ra_out_of_seq = validate_int(n_ra_out_of_seq)

    @n_ra_buf_waits.setter
    def n_ra_buf_waits(self, n_ra_buf_waits: int) -> None:
        self._n_ra_buf_waits = validate_int(n_ra_buf_waits)

    @ra_buf_wait_time.setter
    def ra_buf_wait_time(self, ra_buf_wait_time: int) -> None:
        self._ra_buf_wait_time = validate_int(ra_buf_wait_time)

    @ra_data_latency.setter
    def ra_data_latency(self, ra_data_latency: int) -> None:
        self._ra_data_latency = validate_int(ra_data_latency)

    @avg_ra_data_latency.setter
    def avg_ra_data_latency(self, avg_ra_data_latency: int) -> None:
        self._avg_ra_data_latency = validate_int(avg_ra_data_latency)

    @ddp_readext.setter
    def ddp_readext(self, ddp_readext: int) -> None:
        self._ddp_readext = validate_int(ddp_readext)
