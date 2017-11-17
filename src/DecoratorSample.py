import functools


def printUrl(url):
    print url

def log_decorator(log_enabled=None):
    def actual_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if log_enabled:
                print("Calling Function: " + func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator

@log_decorator
def just_some_function():
    print("Wheee!")

just_some_function()


#
# def dec(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
# return dec
#
# @dec
# dic = {"a" : 1}
