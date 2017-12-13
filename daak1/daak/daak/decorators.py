
__author__ = "davood akbari <daak1365@yahoo.com>"
__status__ = "production"
__version__ = "0.0.0.1"
__date__ = "November 2017"


from daak1.daak.daak import contextManager

from functools import wraps
import inspect

urlMap = {}

def jsonPost(**options):
    def decorator(f):
        print inspect.getmembers(f)#[1][1].__name__
        # print dir(f)
        print f.__self__

        # print inspect.stack()[0][1]
        # rootPath="/home/david/LinuxOther/project/david-project/python/daak-flask/daak-root"
        # filePath = inspect.getfile(f)
        # contextName = filePath[len(rootPath) + 1:]
        # contextName = contextName[: contextName.find('/')]
        # print contextName
        # print(filePath.find(rootPath))

        print contextManager.getContextName(f)

        # print inspect.getmodule(f)
        # print inspect.getsourcefile(f)

        # print dir(f.__self__.__class__)
        # # print get_class_that_defined_method(f)
        # print  f.__self__.__class__
        # print f.im_class.__name__
        # urlMap[f.func_name + '.daak'] = f
        return f
    return decorator













