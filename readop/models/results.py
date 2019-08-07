"""
Contains class for storing operation results.
"""

from readop.utility import validator


class Results:
    """
    Stores operation results obtained through ddboost_stress and the DDVE.
    """

    def __init__(
            self,
            execution_time: int = 0,
            n_ras: int = 0,
            n_ra_cbs: int = 0,
            n_ra_out_of_seq: int = 0,
            n_ra_buf_waits: int = 0,
            ra_buf_wait_time: int = 0,
            ra_data_latency: int = 0,
            avg_ra_data_latency: int = 0,
            ddp_readext: int = 0,
            total_bytes_read: int = 0
    ):
        """
        Initializes the stored values using the provided arguments.

        :param execution_time: Elapsed time in milliseconds required for the operation to complete.
        :param n_ras: Number of times the client has started read ahead.
        :param n_ra_cbs: Number of times read ahead callbacks have been completed. Should be same as n_ras.
        :param n_ra_out_of_seq: Number of reads that were non-sequential.
        :param n_ra_buf_waits: Number of times reads had to wait on internal buffers for read-ahead.
        :param ra_buf_wait_time: Time spent waiting for buffers to become available during reads.
        :param ra_data_latency: Total time spent waiting for all read-aheads to occur. The time used for each read-ahead
        is the time from the start, until the callback is fired.
        :param avg_ra_data_latency: Average time spent waiting for read-aheads, this ends up being your data latency
        divided by the number of read aheads completed.
        :param ddp_readext: This is the name of the DDBoost asynchronous read RPC. The counter from the CLI shows the
        number of these RPCs that have been sent from clients since the last time it has been cleared. The client does
        async reads when doing read-ahead.
        :param total_bytes_read: Total number of bytes read during the operation.
        """

        self.execution_time = execution_time
        self.n_ras = n_ras
        self.n_ra_cbs = n_ra_cbs
        self.n_ra_out_of_seq = n_ra_out_of_seq
        self.n_ra_buf_waits = n_ra_buf_waits
        self.ra_buf_wait_time = ra_buf_wait_time
        self.ra_data_latency = ra_data_latency
        self.avg_ra_data_latency = avg_ra_data_latency
        self.ddp_readext = ddp_readext
        self.total_bytes_read = total_bytes_read

    @property
    def execution_time(self) -> int:
        """
        Elapsed time in milliseconds required for the operation to complete.

        :getter: Gets the elapsed time.
        :setter: Sets the elapsed time.
        """

        return self.__execution_time
    
    @property
    def n_ras(self) -> int:
        """
        Number of times the client has started read ahead.

        :getter: Gets the number of times the client has started read ahead.
        :setter: Sets the number of times the client has started read ahead.
        """

        return self.__n_ras
    
    @property
    def n_ra_cbs(self) -> int:
        """
        Number of times read ahead callbacks have been completed. Should be same as n_ras.

        :getter: Gets the number of times read ahead callbacks have been completed.
        :setter: Sets the number of times read ahead callbacks have been completed.
        """

        return self.__n_ra_cbs
    
    @property
    def n_ra_out_of_seq(self) -> int:
        """
        Number of reads that were non-sequential.

        :getter: Gets the number of reads that were non-sequential.
        :setter: Sets the number of reads that were non-sequential.
        """

        return self.__n_ra_out_of_seq
    
    @property
    def n_ra_buf_waits(self) -> int:
        """
        Number of times reads had to wait on internal buffers for read-ahead.

        :getter: Gets the number of times reads had to wait.
        :setter: Sets the number of times reads had to wait.
        """

        return self.__n_ra_buf_waits
    
    @property
    def ra_buf_wait_time(self) -> int:
        """
        Time spent waiting for buffers to become available during reads.

        :getter: Gets the time spent waiting.
        :setter: Sets the time spent waiting.
        """

        return self.__ra_buf_wait_time
    
    @property
    def ra_data_latency(self) -> int:
        """
        Total time spent waiting for all read-aheads to occur. The time used for each read-ahead is the time from the
        start, until the callback is fired.

        :getter: Gets the time spent waiting for all read-aheads to occur.
        :setter: Sets the time spent waiting for all read-aheads to occur.
        """

        return self.__ra_data_latency
    
    @property
    def avg_ra_data_latency(self) -> int:
        """
        Average time spent waiting for read-aheads, this ends up being your data latency divided by the number of read
        aheads completed.

        :getter: Gets the time spent waiting for read-aheads.
        :setter: Sets the time spent waiting for read-aheads.
        """

        return self.__avg_ra_data_latency
    
    @property
    def ddp_readext(self) -> int:
        """
        This is the name of the DDBoost asynchronous read RPC. The counter from the CLI shows the number of these RPCs
        that have been sent from clients since the last time it has been cleared. The client does async reads when doing
        read-ahead.

        :getter: Gets the number of ddp_readext RPC calls made.
        :setter: Sets the number of ddp_readext RPC calls made.
        """

        return self.__ddp_readext
    
    @property
    def total_bytes_read(self) -> int:
        """
        Total number of bytes read during the operation.

        :getter: Gets the number of bytes read.
        :setter: Sets the number of bytes read.
        """

        return self.__total_bytes_read
    
    @execution_time.setter
    def execution_time(self, execution_time: int) -> None:
        self.__execution_time = validator.validate_int_geq_zero(execution_time)
    
    @n_ras.setter
    def n_ras(self, n_ras: int) -> None:
        self.__n_ras = validator.validate_int_geq_zero(n_ras)
    
    @n_ra_cbs.setter
    def n_ra_cbs(self, n_ra_cbs: int) -> None:
        self.__n_ra_cbs = validator.validate_int_geq_zero(n_ra_cbs)
    
    @n_ra_out_of_seq.setter
    def n_ra_out_of_seq(self, n_ra_out_of_seq: int) -> None:
        self.__n_ra_out_of_seq = validator.validate_int_geq_zero(n_ra_out_of_seq)
    
    @n_ra_buf_waits.setter
    def n_ra_buf_waits(self, n_ra_buf_waits: int) -> None:
        self.__n_ra_buf_waits = validator.validate_int_geq_zero(n_ra_buf_waits)
    
    @ra_buf_wait_time.setter
    def ra_buf_wait_time(self, ra_buf_wait_time: int) -> None:
        self.__ra_buf_wait_time = validator.validate_int_geq_zero(ra_buf_wait_time)
    
    @ra_data_latency.setter
    def ra_data_latency(self, ra_data_latency: int) -> None:
        self.__ra_data_latency = validator.validate_int_geq_zero(ra_data_latency)
    
    @avg_ra_data_latency.setter
    def avg_ra_data_latency(self, avg_ra_data_latency: int) -> None:
        self.__avg_ra_data_latency = validator.validate_int_geq_zero(avg_ra_data_latency)
    
    @ddp_readext.setter
    def ddp_readext(self, ddp_readext: int) -> None:
        self.__ddp_readext = validator.validate_int_geq_zero(ddp_readext)
    
    @total_bytes_read.setter
    def total_bytes_read(self, total_bytes_read: int) -> None:
        self.__total_bytes_read = validator.validate_int_geq_zero(total_bytes_read)
