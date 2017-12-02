from src.daak.daak.context import ContextManager
from os import path


def getContextManager():
    configPath = ContextManager.configPath()
    if path.isfile(configPath):
        config = {}
        execfile(configPath, config)

        rootPath = config.get('rootPath')
        logPath = config.get('logPath')
        if rootPath == None:
            raise ValueError("please set 'rootPath' variables in config file!")

        if logPath == None:
            return ContextManager(rootPath)

        return  ContextManager(rootPath, logPath)

    else:
        raise IOError("file in path '" + configPath + "' not found. pleas create it!")




