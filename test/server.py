#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from test.hello import application

httpd =make_server("", 8765, application)
print("Serving HTTP on port 8000...")
httpd.serve_forever()