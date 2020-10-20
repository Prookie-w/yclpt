#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.find_element import FindElement


class SwdjPage(object):
    def __init__(self, driver):
        self.find_e = FindElement(driver, "SwjdElement")

    def get_swh_element(self):
        self.find_e.get_element("swh")

    def get_bt_element(self):
        self.find_e.get_element("bt")
