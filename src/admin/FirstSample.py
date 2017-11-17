#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.admin import simple_page
from src.daak import JsonDaak
from src.daak.serviceImpDaak import jsonPostDaak

from flask import render_template

@simple_page.route('/json', methods=['POST'])
@jsonPostDaak()
def add_message(a, b):
    # content = request.json
    # print content['mytext']
    # print dd

    class JsonDaak2:
        pass

    ali = JsonDaak2()
    ali.name = "ali"

    me = JsonDaak2()
    me.name = "داود"
    me.age = 35
    me.dog = JsonDaak2()
    me.dog.name = "Apollo"
    me.tople = [1,2,3.4]
    me.dic = {"ali": 1, "mamad":2, "hasn": ali}
    return me#jsonify({"uuid":"david"})


@simple_page.route('/')
def root():
    return render_template('json.html')