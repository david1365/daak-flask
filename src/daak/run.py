from src.daak import flask
from src.admin import simple_page

flask.register_blueprint(simple_page, url_prefix='/admin')

if __name__ == "__main__":
    flask.run(port=8080)