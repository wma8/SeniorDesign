import unittest

from readop.models.parameters import Parameters


class ParametersTest(unittest.TestCase):
    # run before every test
    def setUp(self):
        self.parameters = Parameters()
    
    def test_default_access_pattern(self):
        # test default value
        self.assertEqual(self.parameters.default_access_pattern, 0)
        
        # set valid value
        self.parameters.default_access_pattern = 1
        self.assertEqual(self.parameters.default_access_pattern, 1)
        
        # set invalid value (non-integer)
        with self.assertRaises(TypeError):
            self.parameters.default_access_pattern = 'test'
        
        # set invalid value (negative)
        with self.assertRaises(ValueError):
            self.parameters.default_access_pattern = -1
    
    def test_apd_data_seq_threshold(self):
        # test default value
        self.assertEqual(self.parameters.apd_data_seq_threshold, 0)
        
        # set valid value
        self.parameters.apd_data_seq_threshold = 1
        self.assertEqual(self.parameters.apd_data_seq_threshold, 1)
        
        # set invalid value (non-integer)
        with self.assertRaises(TypeError):
            self.parameters.apd_data_seq_threshold = 'test'
        
        # set invalid value (negative)
        with self.assertRaises(ValueError):
            self.parameters.apd_data_seq_threshold = -1
    
    def test_init_io_region_size(self):
        # test default value
        self.assertEqual(self.parameters.init_io_region_size, 2048)
        
        # set valid value
        self.parameters.init_io_region_size = 1
        self.assertEqual(self.parameters.init_io_region_size, 1)
        
        # set invalid value (non-integer)
        with self.assertRaises(TypeError):
            self.parameters.init_io_region_size = 'test'
        
        # set invalid value (negative)
        with self.assertRaises(ValueError):
            self.parameters.init_io_region_size = -1
    
    def test_max_io_regions(self):
        # test default value
        self.assertEqual(self.parameters.max_io_regions, 16)
        
        # set valid value
        self.parameters.max_io_regions = 1
        self.assertEqual(self.parameters.max_io_regions, 1)
        
        # set invalid value (non-integer)
        with self.assertRaises(TypeError):
            self.parameters.max_io_regions = 'test'
        
        # set invalid value (negative)
        with self.assertRaises(ValueError):
            self.parameters.max_io_regions = -1
    
    def test_apd_access_seq_threshold(self):
        # test default value
        self.assertEqual(self.parameters.apd_access_seq_threshold, 80)
        
        # set valid value
        self.parameters.apd_access_seq_threshold = 1
        self.assertEqual(self.parameters.apd_access_seq_threshold, 1)
        
        # set invalid value (non-integer)
        with self.assertRaises(TypeError):
            self.parameters.apd_access_seq_threshold = 'test'
        
        # set invalid value (negative)
        with self.assertRaises(ValueError):
            self.parameters.apd_access_seq_threshold = -1
    
    def test_apd_access_random_threshold(self):
        # test default value
        self.assertEqual(self.parameters.apd_access_random_threshold, 70)
        
        # set valid value
        self.parameters.apd_access_random_threshold = 1
        self.assertEqual(self.parameters.apd_access_random_threshold, 1)
        
        # set invalid value (non-integer)
        with self.assertRaises(TypeError):
            self.parameters.apd_access_random_threshold = 'test'
        
        # set invalid value (negative)
        with self.assertRaises(ValueError):
            self.parameters.apd_access_random_threshold = -1
    
    def test_apd_access_random_inc_threshold(self):
        # test default value
        self.assertEqual(self.parameters.apd_access_random_inc_threshold, 90)
        
        # set valid value
        self.parameters.apd_access_random_inc_threshold = 1
        self.assertEqual(self.parameters.apd_access_random_inc_threshold, 1)
        
        # set invalid value (non-integer)
        with self.assertRaises(TypeError):
            self.parameters.apd_access_random_inc_threshold = 'test'
        
        # set invalid value (negative)
        with self.assertRaises(ValueError):
            self.parameters.apd_access_random_inc_threshold = -1
