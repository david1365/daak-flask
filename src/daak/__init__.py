# -*- coding: utf-8 -*-
"""
    daak
    ~~~~~

    A microframework based on twisted.  It's extensively documented
    and follows best practice patterns.

    :copyright: (c) 2017 by Davood Akbari.
    :license: GPL, see LICENSE for more details.
"""
__version__ = '0.0.1'

import logging
#
# logging.basicConfig(
#     format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
#     handlers=[
#         logging.FileHandler("{0}/{1}.log".format("/tmp", "test")),
#         logging.StreamHandler()
#     ])
log = logging.getLogger("daak")

urlMap = {}
#
# from flask import Flask
# flask = Flask(__name__)
#
# @flask.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     return response