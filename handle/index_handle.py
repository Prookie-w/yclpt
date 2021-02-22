#!/usr/bin/env python
# -*- coding:utf-8 -*-
from page.index_page import IndexPage
from selenium.webdriver.common.keys import Keys
class IndexHandle(object):
    def __init__(self, driver):
        self.index_page = IndexPage(driver)

    def click_ptsw(self):
        self.index_page.get_ptsw_button().send_keys(Keys.ENTER)

    def click_lwycl(self):
        self.index_page.get_lwycl_button().click()

    def click_cgx(self):
        print(self.index_page.get_cgx_button())
        self.index_page.get_cgx_button().click()
