#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.find_element import FindElement


class IndexPage(object):
    def __init__(self, driver):
        self.find_e = FindElement(driver, "IndexElement")

    def get_index_element(self, ele):
        return self.find_e.get_element(ele)

    def click_index_element(self, ele):
        self.find_e.get_element(ele).click()

    def send_keys_index_element(self, ele, text, clear=False):
        if clear:
            e = self.find_e.get_element(ele)
            e.clear()
            e.send_keys(text)
        else:
            self.find_e.get_element(ele).send_keys(text)
