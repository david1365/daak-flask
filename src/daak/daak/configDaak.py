from src.daak.daak.context import ContextManager

def getContextManager():
    config = {}
    execfile(ContextManager.configPath(), config)

    rootPath = config.get('rootPath')
    logPath = config.get('logPath')
    if rootPath == None:
        raise ValueError("please set 'rootPath' variables in config file!")

    if logPath == None:
        return ContextManager(rootPath)

    return  ContextManager(rootPath, logPath)
