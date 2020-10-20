#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.find_element import FindElement


class IndexPage(object):
    def __init__(self, driver):
        self.find_e = FindElement(driver, "IndexElement")

    def get_ptsw_button(self):
        return self.find_e.get_element("ptsw_button")
