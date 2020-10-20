#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from page.index_page import IndexPage
from page.swdj_page import SwdjPage
from selenium.webdriver.common.keys import Keys


class PtswHandle(object):
    def __init__(self, driver):
        self.index_page = IndexPage(driver)
        self.swdj_page = SwdjPage(driver)

    def click_ptsw(self):
        self.index_page.get_ptsw_button().send_keys(Keys.ENTER)

    def fill_in_form(self, bt):
        #self.swdj_page.get_swh_element().send_keys(swh)
        self.swdj_page.get_bt_element().send_keys(bt)

