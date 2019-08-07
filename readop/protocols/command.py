import subprocess

class Cmd():
    # Allows the user to make a call to the command line
            # and retrieve the result and/or error stream

    def __init__(self, cmd=None):
        cmd = cmd.split()
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (output, err) = process.communicate()
        self.stdout = output
        self.stderr = err