"""
Protocol for sending using dd boost stress and retrieving the results.
"""

import json
import time

import readop.utility.config as config
from readop.protocols.command import Cmd


class StressStats():
    """
    An object for storing the information recieved from a stress test.
    """

    def __init__(self, time=0, n_ras=0, n_ra_cbs=0, n_ra_buf_waits=0, ra_buf_wait_time=0,
            ra_data_latency=0, avg_ra_data_latency=0, n_ra_out_of_seq=0):
        """
        Initializes the object to contain the results from the stress test.
        
        :param time: The time to execute the test.
        :param n_ras: The number of readaheads started.
        :param n_ras_cbs: The number of readaheads call backs completed.
        :param n_ra_buf_waits: The number of buffer waits for readahead.
        :param ra_buf_wait_time: The time spent waiting on buffers for readahead.
        :param ra_data_latency: Total time spent waiting on readahead.
        :param avg_ra_data_latency: Average time spent waiting on readahead.
        :param n_ra_out_of_seq: The number of non-sequential readaheads.
        """
        
        self.time = time
        self.n_ras = n_ras
        self.n_ra_cbs = n_ra_cbs
        self.n_ra_buf_waits = n_ra_buf_waits
        self.ra_buf_wait_time = ra_buf_wait_time
        self.ra_data_latency = ra_data_latency
        self.avg_ra_data_latency = avg_ra_data_latency
        self.n_ra_out_of_seq = n_ra_out_of_seq

    def printStats(self):
        """
        Prints the results object out to std out.
        """

        print('time: ' + str(self.time))
        print('n_ras: ' + str(self.n_ras))
        print('n_ra_cbs: ' + str(self.n_ra_cbs))
        print('n_ra_buf_waits: ' + str(self.n_ra_buf_waits))
        print('ra_buf_wait_time: ' + str(self.ra_buf_wait_time))
        print('ra_data_latency: '+ str(self.ra_data_latency))
        print('avg_ra_data_latency: ' + str(self.avg_ra_data_latency))
        print('n_ra_out_of_seq: ' + str(self.n_ra_out_of_seq))
    
    def getJSON(self):
        """
        Returns the results object as a JSON Object.
        
        :return: The results object as a JSON Object.
        """
        
        return json.dumps(self.__dict__)
    
    def setOperationObject(self, operation):
        """
        Given an operation object, the method sets operation results to the same as this object.
        """
        
        operation.execution_time = self.time
        operation.n_ras = self.n_ras
        operation.n_ra_cbs = self.n_ra_cbs
        operation.n_ra_buf_waits = self.n_ra_buf_waits
        operation.ra_buf_wait_time = self.ra_buf_wait_time
        operation.ra_data_latency = self.ra_data_latency
        operation.avg_ra_data_latency = self.avg_ra_data_latency
        operation.n_ra_out_of_seq = self.n_ra_out_of_seq

class DDBStress():
    """
    This class allows you to execute the stress application
    with default parameters or with parameters that are passed in.
    """
    
    def extractData(self) -> int:
        """
        Gets the data from the output of the stress test and
        sets them to an object that is stored as stats.
        """
        n_ras = None
        n_ra_out_of_seq = 0
        
        lineArray = self.output.decode().split('\n')
        for line in lineArray:
            if 'n_ras:' in line:
                n_ras = int(line.split()[1])
            if 'n_ra_cbs:' in line:
                n_ra_cbs = int(line.split()[1])
            if 'n_ra_buf_waits:' in line:
                n_ra_buf_waits = int(line.split()[1])
            if 'ra_buf_wait_time:' in line:
                ra_buf_wait_time = int(line.split()[1])
            if ' ra_data_latency:' in line:
                ra_data_latency = int(line.split()[1])
            if 'avg_ra_data_latency:' in line:
                avg_ra_data_latency = int(line.split()[1])
            if 'n_ra_out_of_seq:' in line:
                n_ra_out_of_seq = int(line.split()[1])
        
        if n_ras is None:
            raise RuntimeError("There was an error with the stress command: " + self.cmdString)
        
        self.stats = StressStats(self.time, n_ras, n_ra_cbs, n_ra_buf_waits,
                ra_buf_wait_time, ra_data_latency, avg_ra_data_latency, n_ra_out_of_seq) 
        return 0

    def __init__(
            self,
            csvReadFile,
            storageUnit,
            stressFile = '/opt/dell/ddboost_stress',
            readSize = '100M',
            blockSize = '1M',
            hostname = config.get_ddve_host(),
            username = config.get_ddve_username(),
            password = config.get_ddve_password()
    ):
        """
        Initializes the class which executes the stress command and executes it.
        
        :param csvReadFile: The csv file that dictates the read pattern of the test.
        :param storageUnit: The name of the storage unit in the ddve to execute this test in.
        :param stressFile: The path to the stress application. Default is /opt/dell/ddboost_stress.
        :param readSize: The size of the read. Default 100M.
        :param blockSize: THe size the reads are broken down into. Default 1M.
        :param hostname: The name of the ddve host.
        :param username: The username to access the ddve as.
        :param password: The password of the ddve user.
        """

        self.readSize = readSize
        self.blockSize = blockSize
        self.csvReadFile = csvReadFile
        
        self.cmdString = (stressFile + ' -r1 -z' + readSize + ' -b ' + blockSize + ' -d ' + hostname +
                ' -u ' + username + ' -p ' + password + ' -s ' + storageUnit)
        if(csvReadFile != None):
            self.cmdString = self.cmdString + ' -Y ' + csvReadFile
        
        #Starts recording time
        startTime = time.time()
        
        stressCmd = Cmd(self.cmdString)    
        
        #Ends the recording of execution time
        self.time = int(round((time.time() - startTime) * 1000))
        
        self.output = stressCmd.stdout
        self.error = stressCmd.stderr
        #print(self.output)
        self.extractData()
