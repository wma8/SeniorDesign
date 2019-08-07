import unittest
import sys

from io import StringIO

from readop.protocols.ddboost import StressStats
from readop.protocols.ddboost import DDBStress
from readop.database.models import Operation
from readop.models.parameters import Parameters


class TestStressStats(unittest.TestCase):
    def setUp(self):
        # Stores the stats
        self.stressStats = StressStats(1,2,3,4,5,6,7,8)

    def test_stats_init(self):
        # Makes sure they were stored correctly
        self.assertEqual(self.stressStats.time,1)
        self.assertEqual(self.stressStats.n_ras,2)
        self.assertEqual(self.stressStats.n_ra_cbs,3)
        self.assertEqual(self.stressStats.n_ra_buf_waits,4)
        self.assertEqual(self.stressStats.ra_buf_wait_time,5)
        self.assertEqual(self.stressStats.ra_data_latency,6)
        self.assertEqual(self.stressStats.avg_ra_data_latency,7)
        self.assertEqual(self.stressStats.n_ra_out_of_seq,8)

    def test_print_stats(self):
        # Ensures print is formatted correctly
        sys.stdout = mystdout = StringIO()
        self.stressStats.printStats()
        self.assertEqual(mystdout.getvalue(), 'time: 1\nn_ras: 2\nn_ra_cbs: 3\nn_ra_buf_waits:' +
          ' 4\nra_buf_wait_time: 5\nra_data_latency: 6\navg_ra_data_latency: 7\nn_ra_out_of_seq: 8\n')
        sys.stdout = sys.__stdout__

    def test_getJSON(self):
        # Ensures JSON is formatted correctly
        self.assertEqual(self.stressStats.getJSON(), '{"time": 1, "n_ras": 2, "n_ra_cbs": 3, "n_ra_buf_waits":' +
          ' 4, "ra_buf_wait_time": 5, "ra_data_latency": 6, "avg_ra_data_latency": 7, "n_ra_out_of_seq": 8}')

    def test_setOperationObject(self):
        # Ensures the operation object is set correctly
        self.operation = Operation(2, 1, 1, True, Parameters())
        self.stressStats.setOperationObject(self.operation)
        
        self.assertEqual(self.operation.execution_time,1)
        self.assertEqual(self.operation.n_ras,2)
        self.assertEqual(self.operation.n_ra_cbs,3)
        self.assertEqual(self.operation.n_ra_buf_waits,4)
        self.assertEqual(self.operation.ra_buf_wait_time,5)
        self.assertEqual(self.operation.ra_data_latency,6)
        self.assertEqual(self.operation.avg_ra_data_latency,7)
        self.assertEqual(self.operation.n_ra_out_of_seq,8)


class TestDDBStress(unittest.TestCase):

    def setUp(self):
        # Runs a small test of the stress system
        self.ddbstress = DDBStress('/opt/dell/veeam/veeam_bkp_small.csv', 'DDBOOST_STRESS_SU')

    def test_init(self):
        # Ensures the DDBStress class initiated
        self.assertIsNotNone(self.ddbstress)

    def test_extract_data(self):
        # Ensures extract data is completed
        self.ddbstress.extractData()
        self.assertEqual(self.ddbstress.extractData(), 0)


class TestDDBStressError(unittest.TestCase):
    def test_error(self):
        # Runs a small test of the stress system with invalid arguments
        with self.assertRaises(RuntimeError):
            self.ddbstress = DDBStress('DDBOOST_STRESS_SU', '/opt/dell/veeam/veeam_bkp_small.csv')
