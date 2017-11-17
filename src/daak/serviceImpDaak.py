import inspect
from functools import wraps

from flask import request, render_template
from flask.wrappers import _get_data

from src.daak.JsonDaak import JsonDaak


def jsonPostDaak(**options):
    def actualJsonPost(func):
        @wraps(func)
        def wrapperJsonPost(*args, **kwargs):
            cache = options.pop("cache", True)

            funcArgs = inspect.getargspec(func).args
            # request.headers
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
            # result = JsonDaak.toJSON(result)
            # result =  json.loads(result)

            return JsonDaak.toJSON(result) #jsonify(result) #  #if not raw else result

        return wrapperJsonPost
    return actualJsonPost



