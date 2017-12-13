from daak1.daak.daak.context import ContextManager
from os import path

def checkConfigFile(configPath):
    if not path.isfile(configPath):
        raise IOError("file in path '" + configPath + "' not found. pleas create it!")

def execFile(path):
    config = {}
    execfile(path, config)
    return config

def getContextManager():
    configPath = ContextManager.configPath()

    checkConfigFile(configPath)

    config = execFile(configPath)

    rootPath = config.get('rootPath')
    logPath = config.get('logPath')
    if rootPath == None:
        raise ValueError("please set 'rootPath' variables in config file!")

    if logPath == None:
        return ContextManager(rootPath)

    return ContextManager(rootPath, logPath)

def getConfigVariable(configPath):
    checkConfigFile(configPath)

    config = execFile(configPath)

    context = config.get('context')
    service = config.get('service')
    web = config.get('web')

    config = [context, service, web]

    if None in config:
        raise ValueError("please set variables in config file for any project!")

    yield context, service, web





