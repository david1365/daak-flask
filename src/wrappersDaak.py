# -*- coding: utf-8 -*-
"""
    wrappersDaak
    ~~~~~

    :copyright: (c) 2017 by Davood Akbari.
    :license: GPL, see LICENSE for more details.
"""

from flask import Flask as FlaskBase
from werkzeug.datastructures import Headers
from flask.wrappers import Response as ResponseBase


class ResponseDaak(ResponseBase):
    def __init__(self, response=None, status=None, headers=None,
                 mimetype=None, content_type=None, direct_passthrough=False):
        headers = Headers(headers)
        headers.add('Access-Control-Allow-Origin', '*')
        headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        super(ResponseBase, self).__init__(response, status, headers,
                                           mimetype, content_type, direct_passthrough)

class FlaskDaak(FlaskBase):
    pass
    # response_class = ResponseDaak

