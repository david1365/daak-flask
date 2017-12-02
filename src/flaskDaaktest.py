from flask import Flask, Response, current_app, json, request


class ResponseJSON(Response):
    """Extend flask.Response with support for list/dict conversion to JSON."""
    def __init__(self, content=None, *args, **kargs):
        if isinstance(content, (list, dict)):
            kargs['mimetype'] = 'application/json'
            content = to_json(content)

        super(Response, self).__init__(content, *args, **kargs)

    @classmethod
    def force_type(cls, response, environ=None):
        """Override with support for list/dict."""
        if isinstance(response, (list, dict)):
            return cls(response)
        else:
            return super(Response, cls).force_type(response, environ)


def to_json(content):
    """Converts content to json while respecting config1.py options."""
    indent = None
    separators = (',', ':')

    if (current_app.config['JSONIFY_PRETTYPRINT_REGULAR']
        and not request.is_xhr):
        indent = 2
        separators = (', ', ': ')

    return (content.to)


class FlaskJSON(Flask):
    """Extension of standard Flask app with custom response class."""
    response_class = ResponseJSON


app = FlaskJSON(__name__)



# @flask.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     return response




# from werkzeug.wrappers import Response as ResponseBase
# from werkzeug.datastructures import Headers
# from flask.wrappers import Response as ResponseBase

# class ResponseDaak(ResponseBase):
#     def __init__(self, response=None, status=None, headers=None,
#                  mimetype=None, content_type=None, direct_passthrough=False):
#         # # kargs['mimetype'] = 'application/json'
#         # kargs['headers']['Access-Control-Allow-Origin'] = '*'
#         # kargs['headers']['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
#         # kargs['headers']['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
#         self.headers = Headers(headers)
#
#         self.headers.add('Access-Control-Allow-Origin', '*')
#         self.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#         self.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#         super(ResponseBase, self).__init__(response, status, headers,
#                                            mimetype, content_type, direct_passthrough)

