#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base.read_ini import ReadIni
class FindElement(object):
    def __init__(self, driver, node):
        self.driver = driver
        self.node = node

    def split(self, key):
        locator = ReadIni(node=self.node)
        data = locator.get_value(key).split(",")
        lenth = len(data)
        by = data[0]
        value = data[1]
        locator_dict = {
            'id': 'id',
            'name': 'name',
            'class': 'class name',
            'tag': 'tag name',
            'link': 'link text',
            'plink': 'partial link text',
            'xpath': 'xpath',
            'css': 'css selector',
        }
        if by not in locator_dict.keys():
            return None
        if lenth == 2:
            return locator_dict[by], value, None
        elif lenth == 3:
            return locator_dict[by], value, int(data[2])

    def get_element(self, key):
        by, value, num = self.split(key)
        try:
            if num == None:
                return self.driver.find_element(by, value)
            elif isinstance(num, int):
                return self.driver.find_elements(by, value)[num]
            else:
                return None
        except:
            return None

