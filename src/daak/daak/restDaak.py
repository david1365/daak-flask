from functools import wraps
import inspect

urlMap = {}

def jsonPost(**options):
    def decorator(f):
        print inspect.getmembers(f)#[1][1].__name__
        print dir(f)
        # print f.__class__.__name__

        # print inspect.stack()[0][1]
        print inspect.getfile(f)
        print inspect.getmodule(f)
        print inspect.getsourcefile(f)

        # print dir(f.__self__.__class__)
        # # print get_class_that_defined_method(f)
        # print  f.__self__.__class__
        # print f.im_class.__name__
        # urlMap[f.func_name + '.daak'] = f
        return f
    return decorator










