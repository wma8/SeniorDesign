import unittest

import readop.utility.config as config


class ConfigTest(unittest.TestCase):
    def test_get_ddve_host(self):
        self.assertEqual(config.get_ddve_host(), '192.168.41.52')

    def test_get_ddve_username(self):
        self.assertEqual(config.get_ddve_username(), 'sysadmin')

    def test_get_ddve_password(self):
        self.assertEqual(config.get_ddve_password(), 'sdcTeam21')

    def test_get_ddve_rest_port(self):
        self.assertEqual(config.get_ddve_rest_port(), '3009')

    def test_get_database_host(self):
        self.assertEqual(config.get_database_host(), 'localhost')

    def test_get_database_port(self):
        self.assertEqual(config.get_database_host(), '3306')

    def test_get_database_username(self):
        self.assertEqual(config.get_database_username(), 'root')

    def test_get_database_password(self):
        self.assertEqual(config.get_database_password(), 'sdcTeam21!')

    def test_database_name(self):
        self.assertEqual(config.get_database_name(), 'ReadOp')
