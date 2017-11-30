
__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "November 2017"

class Context(object):

    def __init__(self, name, service='service', web='web', logPath='../log/daak.log'):
        self._name = name
        self._service = service
        self._web = web
        self._logPath = logPath

    @property
    def logPath(self):
        return self._logPath

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, value):
    #     self.__name = value

    @property
    def service(self):
        return self._service

    @property
    def web(self):
        return self._web


class ContextManager(object):
    _contexts = {}

    def __init__(self, rootPath, logPath='../log/daak.log'):
        self._rootPath = rootPath
        self._logPath = logPath

    @classmethod
    def add(self, context):
        self._contexts[context.name] = context

    @classmethod
    def get(self, contextName, default=None):
        return self._contexts.get(contextName, default)

    @property
    def rootPath(self):
        return self._rootPath

    @property
    def logPath(self):
        return self._logPath

    @staticmethod
    def configPath():
        return "../../config/config.py"



