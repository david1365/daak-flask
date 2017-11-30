import unittest
from src.daak.daak.context import Context, ContextManager


class TestJsonDaak(unittest.TestCase):
    def test_ContextManager(self):
        contextManager = ContextManager(rootPath='/')
        contextManager.add(context=Context("context1"))
        ctx = contextManager.get("context1")
        self.assertEqual(ctx.service, "service")
        self.assertEqual(ctx.web, "web")
        self.assertEqual(ContextManager.configPath(), "../../config/config.py")

    def test_Context(self):
        context = Context("context1")
        self.assertEqual(context.service, 'service')
        self.assertEqual(context.name, "context1")



if __name__ == '__main__':
    unittest.main()