import unittest
import paramiko

import readop.utility.config as config
from readop.protocols.ddve import DDVEClient


class DDVETest(unittest.TestCase):
    # do a garbage collection in ddve system before start these tests
    # run before every test
    def setUp(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(
            config.get_ddve_host(),
            username=config.get_ddve_username(),
            password=config.get_ddve_password()
        )
        self.ddve = DDVEClient(self.ssh_client)
    
    # run after every test
    def tearDown(self):
        pass
    
    def test_create_storage_unit(self):
        # test default value
        returnMsg = 'Created storage-unit "test-create1" for "sysadmin".'
        lines = self.ddve.createStorageUnit('test-create1', 'sysadmin')
        if len(lines.getOutput().readlines()) != 0:
            line = lines.getOutput().readlines()[0].rstrip()
            self.assertEqual(line, returnMsg)
        else:
            self.assertEqual(0, len(lines.getOutput().readlines()))

        # test create storage unit with same name
        returnMsg = '**** MTree "/data/col1/test-create1" already exists.'
        lines = self.ddve.createStorageUnit('test-create1', 'sysadmin')
        if len(lines.getOutput().readlines()) != 0:
            line = lines.getOutput().readlines()[0].rstrip()
            self.assertEqual(line, returnMsg)
        else:
            self.assertEqual(0, len(lines.getOutput().readlines()))

    def test_check_filesystem_status(self):
        returnMsg = 'The filesystem is enabled and running.'
        lines = self.ddve.checkSystemStatus()
        line = lines.getOutput().readlines()[0].rstrip()
        self.assertEqual(line, returnMsg)
    
    def test_get_storage_units(self):
        returnMsg = 'Name                    Pre-Comp (GiB)   Status   User       Report Physical'
        lines = self.ddve.getStorageUnits()
        line = lines.getOutput().readlines()[0].rstrip()
        self.assertEqual(line, returnMsg)
    
    def test_delete_storage_unit(self):
        # test default value
        returnMsg = 'Storage-unit "test-create1" deleted.'
        lines = self.ddve.deleteStorageUnit('test-create1')
        if len(lines.getOutput().readlines()) != 0:
            line = lines.getOutput().readlines()[0].rstrip()
            self.assertEqual(line, returnMsg)
        else:
            self.assertEqual(0, len(lines.getOutput().readlines()))

    def test_get_mtrees(self):
        returnMsg = 'Name                               Pre-Comp (GiB)   Status'
        lines = self.ddve.getMTrees()
        line = lines.getOutput().readlines()[0].rstrip()
        self.assertEqual(line, returnMsg)

    # Don't test this until data is stored
    # def test_garbage_collection(self):
    #     returnMsg = 'Name                               Pre-Comp (GiB)   Status'
    #     self.assertEqual(self.ddve.garbageCollection, returnMsg)
    
    def test_reset_stats(self):
        returnMsg = 'DD Boost statistics cleared.'
        lines = self.ddve.resetStats()
        line = lines.getOutput().readlines()[0].rstrip()
        self.assertEqual(line, returnMsg)
    
    # def test_get_stats(self):
        # self.assertEqual(self.ddve.getStats, returnMsg)
