import unittest

from readop.managers.ddboost import DDBoostManager
from readop.database.models import Operation
from readop.models.parameters import Parameters


class TestDDBoostManager(unittest.TestCase):
    def setUp(self):
        # Set up the execution of a stress call
        self.manager = DDBoostManager()
        self.operation = Operation(2, 1, 1, True, Parameters())
        self.execute = self.manager.execute(self.operation)

    def test_execute(self):
        # Tests that the object was created
        self.assertIsNotNone(self.manager)
        # Tests that the execution of the command was a success
        self.assertEqual(self.execute, 0)
        # Tests That the class responds with JSON strings
        self.assertTrue(isinstance(self.manager.getStatsJSON(), str))
        # Ensures there were results that were gathered
        self.assertIsNotNone(self.manager.getStats())
