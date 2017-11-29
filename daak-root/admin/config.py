# from flask import Blueprint
#
# simple_page = Blueprint('simple_page', __name__, template_folder='web', static_folder='web')
#
# a = 123
#
from os.path import basename, dirname, join
from glob import glob
pwd = dirname(__file__)
for x in glob(join(pwd, '*.py')):
    if not x.startswith('__'):
        __import__(basename(x)[:-3], globals(), locals())

context="admin"
service="server"
web="static"