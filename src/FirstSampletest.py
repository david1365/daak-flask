#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.admin import simple_page
from src.daak import flask, JsonDaak
from src.daak.serviceImpDaak import jsonPostDaak

from flask import render_template


def route(rule, **options):
    """A decorator that is used to define custom routes for methods in
    FlaskView subclasses. The format is exactly the same as Flask's
    `@app.route` decorator.
    """

    def decorator(f):
        # Put the rule cache on the method itself instead of globally
        if not hasattr(f, '_rule_cache') or f._rule_cache is None:
            f._rule_cache = {f.__name__: [(rule, options)]}
        elif not f.__name__ in f._rule_cache:
            f._rule_cache[f.__name__] = [(rule, options)]
        else:
            f._rule_cache[f.__name__].append((rule, options))

        return f

    return decorator




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




# print __name__


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





# def decor(func):
#      def wrapper(*args, **kwargs):
#         # if args: # If args is not empty.
#         #     args =  [n + "david" for n in args]
#         # if kwargs: # If kwargs is not empty.
#         #     for key in kwargs:
#         #         kwargs[key] += "david"
#
#         jsonData = _get_data(request, True)#request.get_json(force=True) or request.data
#         objects = JsonDaak.fromJson(jsonData)
#
#      # data = data.to_dict()
#         # print jsonify(data)
#         print objects
#
#         print('args - ',args)
#         print('kwargs - ',kwargs)
#
#         print inspect.getargspec(func).args
#
#         print request.get_json(force=True)
#
#         return func(*args, **kwargs)
#
#      return wrapper

@simple_page.route('/json', methods=['POST'])
@jsonPostDaak("kk")
def add_message(a, b):
    # content = request.json
    # print content['mytext']
    # print dd

    ali = JsonDaak()
    ali.name = "ali"

    me = JsonDaak()
    me.name = "داود"
    me.age = 35
    me.dog = JsonDaak()
    me.dog.name = "Apollo"
    me.tople = [1,2,3.4]
    me.dic = {"ali": 1, "mamad":2, "hasn": ali}
    return me#jsonify({"uuid":"david"})





# url_for('static', filename='jquery-3.1.1.min.js')

@simple_page.route('/')
def root():
    return render_template('json.html')

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