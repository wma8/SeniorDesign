import unittest

from readop.models.results import Results


class ResultsTest(unittest.TestCase):
    def setUp(self):
        self.results = Results()
    
    def test_execution_time(self):
        self.assertEqual(self.results.execution_time, 0)
        
        self.results.execution_time = 42
        self.assertEqual(self.results.execution_time, 42)
        
        with self.assertRaises(TypeError):
            self.results.execution_time = 'test'
        
        with self.assertRaises(ValueError):
            self.results.execution_time = -42
    
    def test_n_ras(self):
        self.assertEqual(self.results.n_ras, 0)
        
        self.results.n_ras = 42
        self.assertEqual(self.results.n_ras, 42)
        
        with self.assertRaises(TypeError):
            self.results.n_ras = 'test'
        
        with self.assertRaises(ValueError):
            self.results.n_ras = -42
    
    def test_n_ra_cbs(self):
        self.assertEqual(self.results.n_ra_cbs, 0)
        
        self.results.n_ra_cbs = 42
        self.assertEqual(self.results.n_ra_cbs, 42)
        
        with self.assertRaises(TypeError):
            self.results.n_ra_cbs = 'test'
        
        with self.assertRaises(ValueError):
            self.results.n_ra_cbs = -42
    
    def test_n_ra_out_of_seq(self):
        self.assertEqual(self.results.n_ra_out_of_seq, 0)
        
        self.results.n_ra_out_of_seq = 42
        self.assertEqual(self.results.n_ra_out_of_seq, 42)
        
        with self.assertRaises(TypeError):
            self.results.n_ra_out_of_seq = 'test'
        
        with self.assertRaises(ValueError):
            self.results.n_ra_out_of_seq = -42
    
    def test_n_ra_buf_waits(self):
        self.assertEqual(self.results.n_ra_buf_waits, 0)
        
        self.results.n_ra_buf_waits = 42
        self.assertEqual(self.results.n_ra_buf_waits, 42)
        
        with self.assertRaises(TypeError):
            self.results.n_ra_buf_waits = 'test'
        
        with self.assertRaises(ValueError):
            self.results.n_ra_buf_waits = -42
    
    def test_ra_buf_wait_time(self):
        self.assertEqual(self.results.ra_buf_wait_time, 0)
        
        self.results.ra_buf_wait_time = 42
        self.assertEqual(self.results.ra_buf_wait_time, 42)
        
        with self.assertRaises(TypeError):
            self.results.ra_buf_wait_time = 'test'
        
        with self.assertRaises(ValueError):
            self.results.ra_buf_wait_time = -42
    
    def test_ra_data_latency(self):
        self.assertEqual(self.results.ra_data_latency, 0)
        
        self.results.ra_data_latency = 42
        self.assertEqual(self.results.ra_data_latency, 42)
        
        with self.assertRaises(TypeError):
            self.results.ra_data_latency = 'test'
        
        with self.assertRaises(ValueError):
            self.results.ra_data_latency = -42
    
    def test_avg_ra_data_latency(self):
        self.assertEqual(self.results.avg_ra_data_latency, 0)
        
        self.results.avg_ra_data_latency = 42
        self.assertEqual(self.results.avg_ra_data_latency, 42)
        
        with self.assertRaises(TypeError):
            self.results.avg_ra_data_latency = 'test'
        
        with self.assertRaises(ValueError):
            self.results.avg_ra_data_latency = -42
    
    def test_ddp_readext(self):
        self.assertEqual(self.results.ddp_readext, 0)
        
        self.results.ddp_readext = 42
        self.assertEqual(self.results.ddp_readext, 42)
        
        with self.assertRaises(TypeError):
            self.results.ddp_readext = 'test'
        
        with self.assertRaises(ValueError):
            self.results.ddp_readext = -42
    
    def test_total_bytes_read(self):
        self.assertEqual(self.results.total_bytes_read, 0)
        
        self.results.total_bytes_read = 42
        self.assertEqual(self.results.total_bytes_read, 42)
        
        with self.assertRaises(TypeError):
            self.results.total_bytes_read = 'test'
        
        with self.assertRaises(ValueError):
            self.results.total_bytes_read = -42
