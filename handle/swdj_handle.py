#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from page.swdj_page import SwdjPage
import time
from unit.upload_file import UploadFile


class SwdjHandle(object):
    def __init__(self, driver):
        self.swdj_page = SwdjPage(driver)
        self.driver = driver

    def fill_in_form(self, bt, **form):
        self.swdj_page.click_swdj_element("swh")
        time.sleep(1)
        self.swdj_page.click_swdj_element("swhlist")
        if "lwdw" in form.keys():
            self.swdj_page.send_keys_swdj_element("lwdw", form.get("lwdw"))
            time.sleep(1)
            self.swdj_page.click_swdj_element("lwdwlist")
        if "lwh" in form.keys():
            self.swdj_page.send_keys_swdj_element("lwh", form.get("lwh"))
            time.sleep(1)
            self.swdj_page.click_swdj_element("lwhlist")
        if "lwhm" in form.keys():
            self.swdj_page.send_keys_swdj_element("lwhm", form.get("lwhm"), False)
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
            iframe = self.swdj_page.get_iframe_element()
            self.driver.switch_to.frame(iframe)
            self.swdj_page.get_xzsx_elemenet().click()
            self.swdj_page.get_szsxbutton_element().click()
            self.driver.switch_to.default_content()
        else:
            pass


    def upload_file(self, file_path):
        self.swdj_page.get_bdsc_element().click()
        time.sleep(1)
        UploadFile.upload_one(file_path)

