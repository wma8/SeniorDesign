import unittest

from readop.models.credentials import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.credentials = Credentials('username', 'password')
    
    def test_username(self):
        # valid username
        self.assertEqual(self.credentials.username, 'username')
        
        # set non-string username
        with self.assertRaises(TypeError):
            self.credentials.username = 1
        
        # set empty username
        with self.assertRaises(ValueError):
            self.credentials.username = ''
    
    def test_password(self):
        # valid password
        self.assertEqual(self.credentials.password, 'password')
        
        # set non-string password
        with self.assertRaises(TypeError):
            self.credentials.password = 1
        
        # set empty password
        with self.assertRaises(ValueError):
            self.credentials.password = ''
