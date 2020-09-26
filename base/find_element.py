#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.read_ini import ReadIni
class FindElement(object):
    def __init__(self, driver, node):
        self.driver = driver
        self.node = node

    def get_element(self, key):
        read_ini = ReadIni(node=self.node)
        data =read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == "name":
                return self.driver.find_element_by_name(value)
            elif by == "class_name":
                return self.driver.find_element_by_class_name(value)
            elif by == "tag_name":
                return self.driver.find_element_by_tag_name(value)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
            elif by == "link_text":
                return self.driver.find_element_by_link_text(value)
            elif by == "partial_link_text":
                return self.driver.find_element_by_partial_link_text(value)
            elif by =="css_selector":
                return self.driver.find_element_by_css_selector(value)
        except:
            return None


