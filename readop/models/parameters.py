"""
Contains class for storing ddboost Parameters.
"""

from readop.utility import validator


class Parameters:
    """
    Stores ddboost parameters.
    """

    PARAMETER_LIST_LEN: int = 7

    DEFAULT_ACCESS_PATTERN: int = 0
    APD_DATA_SEQ_THRESHOLD: int = 0
    INIT_IO_REGION_SIZE: int = 2048
    MAX_IO_REGIONS: int = 16
    APD_ACCESS_SEQ_THRESHOLD: int = 80
    APD_ACCESS_RANDOM_THRESHOLD: int = 70
    APD_ACCESS_RANDOM_INC_THRESHOLD: int = 90

    def __init__(
        self,
        default_access_pattern: int = DEFAULT_ACCESS_PATTERN,
        apd_data_seq_threshold: int = APD_DATA_SEQ_THRESHOLD,
        init_io_region_size: int = INIT_IO_REGION_SIZE,
        max_io_regions: int = MAX_IO_REGIONS,
        apd_access_seq_threshold: int = APD_ACCESS_SEQ_THRESHOLD,
        apd_access_random_threshold: int = APD_ACCESS_RANDOM_THRESHOLD,
        apd_access_random_inc_threshold: int = APD_ACCESS_RANDOM_INC_THRESHOLD
    ):
        """
        Initializes the stored values using the provided arguments.

        :param default_access_pattern: Initial pattern mode (0 = sequential, 1 = random, 2 = random-incremental).
        :param apd_data_seq_threshold: Threshold for data accesses to be considered sequential.
        :param init_io_region_size: Initial (minimum) APD region size in MB.
        :param max_io_regions: Max APD regions to detect in a file.
        :param apd_access_seq_threshold: Percentage of IOs needed to trigger sequential mode.
        :param apd_access_random_threshold: Percentage of IOs needed to trigger random mode.
        :param apd_access_random_inc_threshold: Percentage of IOs needed to trigger random-incremental mode.
        """

        self.default_access_pattern = default_access_pattern
        self.apd_data_seq_threshold = apd_data_seq_threshold
        self.init_io_region_size = init_io_region_size
        self.max_io_regions = max_io_regions
        self.apd_access_seq_threshold = apd_access_seq_threshold
        self.apd_access_random_threshold = apd_access_random_threshold
        self.apd_access_random_inc_threshold = apd_access_random_inc_threshold
    
    @property
    def default_access_pattern(self) -> int:
        """
        Initial pattern mode (0 = sequential, 1 = random, 2 = random-incremental).

        :getter: Gets the initial pattern mode.
        :setter: Sets the initial pattern mode.
        """

        return self.__default_access_pattern
    
    @property
    def apd_data_seq_threshold(self) -> int:
        """
        Threshold for data accesses to be considered sequential.

        :getter: Gets the data sequential threshold.
        :setter: Sets the data sequential threshold.
        """

        return self.__apd_data_seq_threshold
    
    @property
    def init_io_region_size(self) -> int:
        """
        Initial (minimum) APD region size in MB.

        :getter: Gets the initial APD region size.
        :setter: Sets the initial APD region size.
        """

        return self.__init_io_region_size
    
    @property
    def max_io_regions(self) -> int:
        """
        Max APD regions to detect in a file.

        :getter: Gets the max APD regions.
        :setter: Sets the max APD regions.
        """

        return self.__max_io_regions
    
    @property
    def apd_access_seq_threshold(self) -> int:
        """
        Percentage of IOs needed to trigger sequential mode.

        :getter: Gets the sequential access threshold.
        :setter: Sets the sequential access threshold.
        """

        return self.__apd_access_seq_threshold
    
    @property
    def apd_access_random_threshold(self) -> int:
        """
        Percentage of IOs needed to trigger random mode.

        :getter: Gets the random access threshold.
        :setter: Sets the random access threshold.
        """

        return self.__apd_access_random_threshold
    
    @property
    def apd_access_random_inc_threshold(self) -> int:
        """
        Percentage of IOs needed to trigger random-incremental mode.

        :getter: Gets the random-incremental access threshold.
        :setter: Sets the random-incremental access threshold.
        """

        return self.__apd_access_random_inc_threshold
    
    @default_access_pattern.setter
    def default_access_pattern(self, default_access_pattern: int):
        self.__default_access_pattern = validator.validate_int_geq_zero(default_access_pattern)
    
    @apd_data_seq_threshold.setter
    def apd_data_seq_threshold(self, apd_data_seq_threshold: int):
        self.__apd_data_seq_threshold = validator.validate_int_geq_zero(apd_data_seq_threshold)
    
    @init_io_region_size.setter
    def init_io_region_size(self, init_io_region_size: int):
        self.__init_io_region_size = validator.validate_int_geq_zero(init_io_region_size)
    
    @max_io_regions.setter
    def max_io_regions(self, max_io_regions: int):
        self.__max_io_regions = validator.validate_int_geq_zero(max_io_regions)
    
    @apd_access_seq_threshold.setter
    def apd_access_seq_threshold(self, apd_access_seq_threshold: int):
        self.__apd_access_seq_threshold = validator.validate_int_geq_zero(apd_access_seq_threshold)
    
    @apd_access_random_threshold.setter
    def apd_access_random_threshold(self, apd_access_random_threshold: int):
        self.__apd_access_random_threshold = validator.validate_int_geq_zero(apd_access_random_threshold)
    
    @apd_access_random_inc_threshold.setter
    def apd_access_random_inc_threshold(self, apd_access_random_inc_threshold: int):
        self.__apd_access_random_inc_threshold = validator.validate_int_geq_zero(apd_access_random_inc_threshold)

    @classmethod
    def from_list(cls, parameter_list: list):
        length = len(parameter_list)
        if length != 7:
            raise ValueError(
                'Parameter list must have {0} elements, {1} provided.'.format(
                    str(Parameters.PARAMETER_LIST_LEN),
                    str(length)
                )
            )
        
        return cls(
            parameter_list[0],
            parameter_list[1],
            parameter_list[2],
            parameter_list[3],
            parameter_list[4],
            parameter_list[5],
            parameter_list[6]
        )

    def __repr__(self):
        return (
            'Parameters {\n'
            '    default_access_pattern:          ' + str(self.default_access_pattern) + '\n'
            '    apd_data_seq_threshold:          ' + str(self.apd_data_seq_threshold) + '\n'
            '    init_io_region_size:             ' + str(self.init_io_region_size) + '\n'
            '    max_io_regions:                  ' + str(self.max_io_regions) + '\n'
            '    apd_access_seq_threshold:        ' + str(self.apd_access_seq_threshold) + '\n'
            '    apd_access_random_threshold:     ' + str(self.apd_access_random_threshold) + '\n'
            '    apd_access_random_inc_threshold: ' + str(self.apd_access_random_inc_threshold) + '\n'
            '}'
        )
