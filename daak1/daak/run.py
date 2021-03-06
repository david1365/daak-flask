from flask import request

from daak1.admin import simple_page
from daak1.daak import flask


class ReverseProxied(object):
    '''Wrap the application in this middleware and configure the
    front-end server to add these headers, to let you quietly bind
    this to a URL other than / and to an HTTP scheme that is
    different than what is used locally.

    In nginx:
    location /myprefix {
        proxy_pass http://192.168.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Scheme $scheme;
        proxy_set_header X-Script-Name /myprefix;
        }

    :param app: the WSGI application
    '''
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['PATH_INFO'] = environ['PATH_INFO'][:1]
        script_name = environ.get('HTTP_X_SCRIPT_NAME', '')
        if script_name:
            environ['SCRIPT_NAME'] = script_name
            path_info = environ['PATH_INFO']
            if path_info.startswith(script_name):
                environ['PATH_INFO'] = path_info[len(script_name):]

        scheme = environ.get('HTTP_X_SCHEME', '')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)



# flask.wsgi_app = ReverseProxied(flask.wsgi_app)

flask.register_blueprint(simple_page, url_prefix='/admin')

@flask.before_request
def befor_request():
    request.path

flask.route("/")
def index():
    return "hello iran"

if __name__ == "__main__":
    flask.run(host='127.0.0.1')#'''port=8080''')