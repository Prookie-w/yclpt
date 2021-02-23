#!/usr/bin/env python
# -*- coding:utf-8 -*-
from page.index_page import IndexPage
from selenium.webdriver.common.keys import Keys
class IndexHandle(object):
    def __init__(self, driver):
        self.index_page = IndexPage(driver)

    def click_ptsw(self):
        self.index_page.send_keys_index_element("ptsw_button", Keys.ENTER)

    def click_lwycl(self):
        self.index_page.click_index_element("lwycl_button")

    def click_cgx(self):
        self.index_page.click_index_element("cgx_button")

    def get_ele(self, ele):
        return self.index_page.get_index_element(ele)
