#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "gjx"

'''
webapp
'''

import logging;logging.basicConfig(level=logging.INFO)

import os,json,time
from datetime import datetime
from aiohttp import web

def index(requset):
    return web.Response(headers={'content-type':'text/html'},body = b'<h1>hello world</h1>')

app = web.Application()
app.add_routes([web.get('/',index)])
web.run_app(app,host='127.0.0.1',port=9000)