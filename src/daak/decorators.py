from functools import wraps
from src.daak import urlMap

# def jsonPostDaak(fucn):
#     def actualJsonPost(func):
#         # @wraps(func)
#         # def wrapperJsonPost(*args, **kwargs):
#         urlMap[func.__name_ + '.daak'] = func
#
#
#             # return func(*args, **kwargs)
#
#         return actualJsonPost
#     return actualJsonPost

# def jsonPostDaak(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         urlMap[func.__name_ + '.daak'] = func
#         return func(*args, **kwargs)
#     return wrapper




# def jsonPostDaak(method):
#     def jsonPostDaakDec(*args, **kwargs):
#         urlMap[method.__name_ + '.daak'] = f
#         return method(*args, **kwargs)
#     return jsonPostDaakDec

def route(rule, **options):
    def decorator(f):
        urlMap[f.func_name + '.daak'] = f
        return f
    return decorator

