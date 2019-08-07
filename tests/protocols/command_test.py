import unittest

from readop.protocols.command import Cmd


class TestCmd(unittest.TestCase):
    def setUp(self):
        # Runs a simple command
        self.command = Cmd("echo Hello")
    
    def test_command_output(self):
        # Tests for the correct output
        self.assertEqual(self.command.stdout, b'Hello\n')
    
    def test_command_error(self):
        # Tests for the correct error output
        self.assertEqual(self.command.stderr, b'')
