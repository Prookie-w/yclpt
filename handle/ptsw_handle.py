#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from page.index_page import IndexPage
from page.swdj_page import SwdjPage
from selenium.webdriver.common.keys import Keys
import time
from unit.upload_file import UploadFile


class PtswHandle(object):
    def __init__(self, driver):
        self.index_page = IndexPage(driver)
        self.swdj_page = SwdjPage(driver)

    def click_ptsw(self):
        self.index_page.get_ptsw_button().send_keys(Keys.ENTER)

    def fill_in_form(self, bt, **form):
        self.swdj_page.get_bt_element().send_keys(bt)
        self.swdj_page.get_swh_element().click()
        time.sleep(1)
        self.swdj_page.get_swhlist_element().click()
        if "lwdw" in form.keys():
            self.swdj_page.get_lwdw_element().send_keys(form.get("lwdw"))
            time.sleep(1)
            self.swdj_page.get_lwdwlist_element().click()
        if "lwh" in form.keys():
            self.swdj_page.get_lwh_element().send_keys(form.get("lwh"))
            time.sleep(1)
            self.swdj_page.get_lwhlist_element().click()
        if "lwhm" in form.keys():
            self.swdj_page.get_lwhm_element().clear()
            self.swdj_page.get_lwhm_element().send_keys(form.get("lwhm"))
        if "btlx" in form.keys():
            if 'psj' == form.get("btlx"):
                self.swdj_page.get_psj_element().click()
            elif 'nbd' == form.get("btlx"):
                self.swdj_page.get_nbd_element().click()

    def upload_file(self, file_path):
        self.swdj_page.get_bdsc_element().click()
        time.sleep(1)
        UploadFile.upload_one(file_path)

