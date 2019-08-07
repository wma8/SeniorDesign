import unittest
from types import SimpleNamespace

from readop.models.credentials import Credentials
from readop.utility import validator


class ValidatorTest(unittest.TestCase):
    def test_validate_string(self):
        self.assertEqual(validator.validate_string('test'), 'test')
        
        with self.assertRaises(TypeError):
            validator.validate_string(42)
        
        with self.assertRaises(TypeError):
            validator.validate_string(True)
    
    def test_validate_string_not_empty(self):
        self.assertEqual(validator.validate_string_not_empty('test'), 'test')
        
        with self.assertRaises(ValueError):
            validator.validate_string_not_empty('')
    
    def test_validate_int(self):
        self.assertEqual(validator.validate_int(42), 42)
        
        with self.assertRaises(TypeError):
            validator.validate_int('test')
    
    def test_validate_int_geq_zero(self):
        self.assertEqual(validator.validate_int_geq_zero(42), 42)
        
        with self.assertRaises(ValueError):
            validator.validate_int_geq_zero(-42)
    
    def test_validate_bool(self):
        self.assertEqual(validator.validate_bool(True), True)
        
        with self.assertRaises(TypeError):
            validator.validate_bool('test')

    def test_validate_credentials(self):
        credentials = Credentials('username', 'password')

        self.assertEqual(validator.validate_credentials(credentials), credentials)

        no_username = SimpleNamespace(password='test')
        no_password = SimpleNamespace(username='test')
        int_username = SimpleNamespace(username=123, password='test')
        int_password = SimpleNamespace(username='test', password=123)
        empty_username = SimpleNamespace(username='', password='test')

        with self.assertRaises(AttributeError):
            validator.validate_credentials(no_username)

        with self.assertRaises(AttributeError):
            validator.validate_credentials(no_password)

        with self.assertRaises(TypeError):
            validator.validate_credentials(int_username)

        with self.assertRaises(TypeError):
            validator.validate_credentials(int_password)

        with self.assertRaises(ValueError):
            validator.validate_credentials(empty_username)
