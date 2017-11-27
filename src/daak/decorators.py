from functools import wraps
from src.daak import urlMap
import inspect

def jsonPost(**options):
    def decorator(f):
        print inspect.getmembers(f)#[1][1].__name__
        # print f.im_class.__name__
        # urlMap[f.func_name + '.daak'] = f
        return f
    return decorator

