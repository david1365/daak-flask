from flask import Flask, request, jsonify, json, g
from functools import wraps
import inspect

from flask.wrappers import _get_data

from src.DaakPortal.JsonDaak import JsonDaak

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace




# from werkzeug.routing import BaseConverter
#
# class ListConverter(BaseConverter):
#
#     def to_python(self, value):
#         return value.split('+')
#
#     def to_url(self, values):
#         return '+'.join(BaseConverter.to_url(value)
#                         for value in values)

flask = Flask(__name__)


# print __name__


from os.path import basename, dirname, join
from glob import glob

# pwd = dirname(__file__)
# print glob(join(pwd, '*.py'))

# @flask.route("/")
# def hello():
#     return "Hello World!"
#

#

# def jsonPost(func):
#
#     if not request.is_json:
#         pass#abort(400)
#
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         raw = False
#         if "raw" in kwargs:
#             raw = kwargs["raw"]
#             del kwargs["raw"]
#         result = func(*args, **kwargs)
#         return jsonify(result) if not raw else result
#     return wrapper

def jsonPost(url=None, cache=True):
    def actualJsonPost(func):
        @wraps(func)
        def wrapperJsonPost(*args, **kwargs):
            funcArgs = inspect.getargspec(func).args
            jsonData = _get_data(request, cache)
            objects = JsonDaak.fromJson(jsonData)

            for key in funcArgs:
                if key in objects:
                    kwargs[key] = getattr(objects, key)

            # raw = False
            # if "raw" in kwargs:
            #     raw = kwargs["raw"]
            #     del kwargs["raw"]

            result = func(*args, **kwargs)
            return JsonDaak.toJSON(result) #if not raw else result

        return wrapperJsonPost
    return actualJsonPost



def decor(func):
     def wrapper(*args, **kwargs):
        # if args: # If args is not empty.
        #     args =  [n + "david" for n in args]
        # if kwargs: # If kwargs is not empty.
        #     for key in kwargs:
        #         kwargs[key] += "david"

        jsonData = _get_data(request, True)#request.get_json(force=True) or request.data
        objects = JsonDaak.fromJson(jsonData)

     # data = data.to_dict()
        # print jsonify(data)
        print objects

        print('args - ',args)
        print('kwargs - ',kwargs)

        print inspect.getargspec(func).args

        print request.get_json(force=True)

        return func(*args, **kwargs)

     return wrapper

@flask.route('/json', methods=['POST'])
@jsonPost
def add_message(a, b):
    # content = request.json
    # print content['mytext']
    # print dd

    ali = JsonDaak()
    ali.name = "ali"

    me = JsonDaak()
    me.name = "Onur"
    me.age = 35
    me.dog = JsonDaak()
    me.dog.name = "Apollo"
    me.tople = [1,2,3.4]
    me.dic = {"ali": 1, "mamad":2, "hasn": ali}
    return me#jsonify({"uuid":"david"})



# @flask.before_request
# def before_request():
#     g.data = request.get_json() or request.values

# @flask.route('/json', methods=['POST'])
# def json():
#     return jsonify(request.json)

# @flask.route('/')
# def hello2():
#     return "Hello david!"



# @flask.route('/', defaults={'path': ''})
# @flask.route('/<path:path>')
# def catch_all(path):
#     return 'You want path: %s' % eval(path)()
#
# def david():
#     return 123

if __name__ == "__main__":
    flask.run()







# from flask import jsonify
# from functools import wraps
#
# def jsonify_or_raw(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         raw = False
#         if "raw" in kwargs:
#             raw = kwargs["raw"]
#             del kwargs["raw"]
#         result = func(*args, **kwargs)
#         return jsonify(result) if not raw else result
#     return wrapper
#
# You would use the decorator like so:
#
# @flask.route('/promoters/<int:id>', methods=['GET'])
# @jsonify_or_raw
# def get_promoter(id):
#     return {"your data": "goes here"}


# return standard json
# from flask import json
#
# @flask.route('/summary')
# def summary():
#     data = make_summary()
#     response = flask.response_class(
#         response=json.dumps(data),
#         status=200,
#         mimetype='application/json'
#     )
#     return response