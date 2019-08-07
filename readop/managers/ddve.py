"""
Class to retrieve data from ddve system.
"""
import sys
import paramiko
import json

import readop.utility.config as config
from readop.protocols.ddve import DDVEClient

def retrieveResultFromStats(ddve):
    """
    Retrieve results from the stats in ddve system.

    :param ddve: the ddve class to execute commands
    :return: Two parameters DDP_READEXT and Total bytes read from the stats
    """
    lines = ddve.getStats().getOutput()
    ddpReadExt = ''
    totalBytes = ''
    for line in lines.readlines():
        if 'DDP_READEXT' in line.strip():
            ddpReadExt = line.strip()
        if 'Total bytes read' in line.strip():
            totalBytes = line.strip()
    
    ddpReadExtresult = ddpReadExt.split()
    totalBytesResult = totalBytes.split()

    result = {
        'DDP_READEXT' : ddpReadExtresult[2],
        'Total bytes read' : totalBytesResult[3]
    }

    return result

class DDVEManager:
    """
    Maintains the subsystems required for the operations in ddve.
    """

    def __init__(self):
        """
        Initializes the subsystems required for the operations in ddve.
        """
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(
            config.get_ddve_host(),
            username=config.get_ddve_username(),
            password=config.get_ddve_password()
        )
        self.ddve = DDVEClient(self.ssh_client)

    def clear_results(self):
        """
        Reset the stats in ddve system.

        :return: None.
        """
        lines = self.ddve.checkSystemStatus()

        enabledSystem = False
        enabledString = 'The filesystem is enabled and running'

        for line in lines.getOutput().readlines():
            #print(line.strip())
            if enabledString in line:
                enabledSystem = True

        if enabledSystem:
            self.ddve.resetStats()
    
    def get_results(self, operation):
        """
        Retrieving results from ddve and pass it to the operation subsystems in the proper order.

        :param operation: operation inputs and storage for outputs.
        :return: None, modifies the operation object by reference.
        """
        lines = self.ddve.checkSystemStatus()

        enabledSystem = False
        enabledString = 'The filesystem is enabled and running'

        for line in lines.getOutput().readlines():
            if enabledString in line:
                enabledSystem = True

        if enabledSystem:
            resultGenerated = retrieveResultFromStats(self.ddve)
            operation.ddp_readext = int(resultGenerated['DDP_READEXT'])
            operation.total_bytes_read = int(resultGenerated['Total bytes read'].replace(',', ''))
        
