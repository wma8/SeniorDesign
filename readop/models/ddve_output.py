"""
Class for output message storing from ddve system.
"""
class DDVEOutput:
    """
    Maintains the messages of executing commands in ddve system.
    """
    def __init__(self, inputValue, outputValue, errorValue):
        """
        Initializes the messages of executing commands in ddve system.
        """
        self.inputValue = inputValue
        self.outputValue = outputValue
        self.errorValue = errorValue
    
    def getInput(self):
        """
        Return input message from the commands.

        :return: Input message of the command.
        """
        return self.inputValue

    def getOutput(self):
        """
        Return output message from executing the commands.

        :return: Output message of executing the commands.
        """
        return self.outputValue
    
    def getErrors(self):
        """
        Return error message in executing the commands.

        :return: Error message in executing the commands.
        """
        return self.errorValue
