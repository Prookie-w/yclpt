#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.browser_driver import BrowserDriver
import os
def open(cls):
    browser = BrowserDriver(cls)
    browser.open_browser("360", "http://172.23.23.223:8080/yclpt/")

open()