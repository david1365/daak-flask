
__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "November 2017"


import unittest

from src.daak.daak.configManager import getContextManager
from src.daak.daak.context import ContextManager


class TestJsonDaak(unittest.TestCase):
    def test_configFileNotFound(self):
        try:
            contextManager =  getContextManager()

            self.fail(msg="dont raise exception file not found")
        except Exception as e:
            configPath = ContextManager.configPath()
            self.assertEqual(e.message, "file in path '" + configPath + "' not found. pleas create it!")


    def test_ContextManager(self):
        try:
            contextManager =  getContextManager()

            self.fail(msg="dont raise exception file not found")
        except Exception as e:
            configPath = ContextManager.configPath()
            self.assertEqual(e.message, "please set 'rootPath' variables in config file!")

if __name__ == '__main__':
    unittest.main()