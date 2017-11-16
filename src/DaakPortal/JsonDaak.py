from __future__ import print_function
from flask import json, jsonify

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace

class JsonDaak:
    @staticmethod
    def toJSON(object):
        return json.dumps(object, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def fromJson(jsonData):
        return json.loads(jsonData, object_hook=lambda d: Namespace(**d))
