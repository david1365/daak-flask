
__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "November 2017"

import inspect
import os.path
import daak1
from os import walk
from daak1.daak.daak.configManager import getConfigVariable

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

        self._init()

    def add(self, contextName, context):
        self._contexts[contextName] = context

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
        appPath = ContextManager.applicationPath()
        return appPath + "config/config.py"

    @staticmethod
    def applicationPath():
        appPath = os.path.abspath(daak1.__file__)
        return daak1.__file__[:appPath.find('__init__.py')]

    def getContextName(self, object):
        filePath = inspect.getfile(object)
        contextName = filePath[len(self._rootPath) + 1:]
        return contextName[: contextName.find('/')]

    def getContext(self, object):
        return self.get(self.getContextName(object))

    def _init(self):
        root, dirs, files = next(walk(self._rootPath))
        for dirName in dirs:
            context, service, web = getConfigVariable(dirName + "config.py")
            self.add(dirName, Context(context, service, web))






