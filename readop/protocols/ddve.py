"""
Interactions with DDVE Parameter system by retrieving results.
"""


from readop.models.ddve_output import DDVEOutput


class DDVEClient:
    """
    Handles credential management and re-authentication for ssh communication.
    """
    def __init__(self, ddve):
        """
        Initialize the ddve protocol instance.
        """
        self.ddve = ddve
    
    def createStorageUnit(self, su_name, user):
        """
        Returns the message for creating a storage unit.

        :param su_name: name of this storage unit
        :param user: user the storage unit is created for
        :return: lines containing the return message from correlated command in ddve
        """
        stdin,stdout,stderr = self.ddve.exec_command("ddboost storage-unit create %s user %s" % (su_name, user))
        lines = DDVEOutput(stdin, stdout, stderr)
        
        return lines

    def deleteStorageUnit(self, su_name):
        """
        Returns the message for deleting a storage unit.

        :param su_name: name of this storage unit
        :return: lines containing the return message from correlated command in ddve
        """
        stdin,stdout,stderr = self.ddve.exec_command("ddboost storage-unit delete %s" % (su_name))
        stdin.write("yes")
        lines = DDVEOutput(stdin, stdout, stderr)
        return lines

    def getStorageUnits(self):
        """
        Returns the message for retrieving a storage unit.

        :return: lines containing the return message from correlated command in ddve
        """
        # System is ready to retrieve data
        stdin,stdout,stderr = self.ddve.exec_command("ddboost storage-unit show")

        lines = DDVEOutput(stdin, stdout, stderr)
        return lines

    def getMTrees(self):
        """
        Returns the message for retrieving the MTrees.

        :return: lines containing the return message from correlated command in ddve
        """
        # System is ready to retrieve data
        stdin,stdout,stderr = self.ddve.exec_command("mtree list")

        lines = DDVEOutput(stdin, stdout, stderr)
        return lines

    def garbageCollection(self):
        """
        Returns the message for doing garbage collection.

        :return: lines containing the return message from correlated command in ddve
        """
        stdin,stdout,stderr = self.ddve.exec_command("filesys clean start")

        lines = DDVEOutput(stdin, stdout, stderr)
        return lines

    def resetStats(self):
        """
        Returns the message for resetting the stats in ddve system.

        :return: lines containing the return message from correlated command in ddve
        """
        # System is ready to retrieve data
        stdin,stdout,stderr = self.ddve.exec_command("ddboost reset stats")

        lines = DDVEOutput(stdin, stdout, stderr)
        return lines

    def getStats(self):
        """
        Returns the message for retrieving the stats data from ddve system.

        :return: lines containing the return message from correlated command in ddve
        """
        # System is ready to retrieve data
        stdin,stdout,stderr = self.ddve.exec_command("ddboost show stats")

        lines = DDVEOutput(stdin, stdout, stderr)
        return lines

    def checkSystemStatus(self):
        """
        Returns the message for checking system status.

        :return: lines containing the return message from correlated command in ddve
        """
        # System is ready to retrieve data
        stdin,stdout,stderr = self.ddve.exec_command("filesys status")

        lines = DDVEOutput(stdin, stdout, stderr)
        return lines
