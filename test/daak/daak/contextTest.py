
__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "November 2017"


import unittest
from daak1.daak.daak.context import Context, ContextManager


class TestJsonDaak(unittest.TestCase):
    def test_ContextManager(self):
        contextManager = ContextManager(rootPath='/')
        contextManager.add(context=Context("context1"))
        ctx = contextManager.get("context1")
        self.assertEqual(ctx.service, "service")
        self.assertEqual(ctx.web, "web")
        # self.assertEqual(ContextManager.configPath(), "../../config/config1.py")

    def test_Context(self):
        context = Context("context1")
        self.assertEqual(context.service, 'service')
        self.assertEqual(context.name, "context1")



if __name__ == '__main__':
    unittest.main()