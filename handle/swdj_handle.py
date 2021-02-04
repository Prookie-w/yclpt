#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from page.swdj_page import SwdjPage
import time
from unit.upload_file import UploadFile


class SwdjHandle(object):
    def __init__(self, driver):
        self.swdj_page = SwdjPage(driver)

    def fill_in_form(self, bt, **form):
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
        self.swdj_page.get_bt_element().send_keys(bt)
        #self.swdj_page.get_mj_element().click()
        time.sleep(1)
        #self.swdj_page.get_mjlist_element().click()
        if "fs" in form.keys():
            num = self.swdj_page.get_fs_element()
            num.clear()
            num.send_keys(form.get("fs"))
        if "bq" in form.keys():
            self.swdj_page.get_bq_element().send_keys(form.get("bq"))

    def fill_dept(self, yysx, **deptInfo):
        if yysx == True:
            self.swdj_page.get_yysx_element().click()
        else:
            pass


    def upload_file(self, file_path):
        self.swdj_page.get_bdsc_element().click()
        time.sleep(1)
        UploadFile.upload_one(file_path)

