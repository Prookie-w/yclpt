#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.ptsw_handle import PtswHandle

class PtswBuiness(object):
    def __init__(self, driver):
        self.ptsw = PtswHandle(driver)

    def ptsw_save(self):
        self.ptsw.click_ptsw()
        self.ptsw.fill_in_form("123456")
