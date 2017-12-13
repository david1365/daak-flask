
__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "November 2017"


import unittest

from daak1.daak.daak.configManager import getContextManager, getConfigVariable
from daak1.daak.daak.context import ContextManager


class TestConfig(unittest.TestCase):
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

            self.fail(msg="dont raise exception rootPath not found")
        except Exception as e:
            self.assertEqual(e.message, "please set 'rootPath' variables in config file!")


    def test_ConfigVariable(self):
        try:
            context, service, web = next(getConfigVariable("../../config/projectConfig1.py"))

            self.fail(msg="dont raise exception variable none")
        except Exception as e:
            self.assertEqual(e.message, "please set variables in config file for any project!")

        try:
            context, service, web = next(getConfigVariable("a.py"))

            self.fail(msg="dont raise exception file not found")
        except Exception as e:
            self.assertEqual(e.message, "file in path 'a.py' not found. pleas create it!")



if __name__ == '__main__':
    unittest.main()