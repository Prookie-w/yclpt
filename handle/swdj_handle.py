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
            self.swdj_page.send_keys_swdj_element("lwhm", form.get("lwhm"), True)
        if "btlx" in form.keys():
            if 'psj' == form.get("btlx"):
                self.swdj_page.click_swdj_element("psj")
            elif 'nbd' == form.get("btlx"):
                self.swdj_page.click_swdj_element("nbd")
            self.swdj_page.click_swdj_element("psld")

        self.swdj_page.send_keys_swdj_element("bt", bt)
        #self.swdj_page.click_swdj_element("mj")
        time.sleep(1)
        #self.swdj_page.click_swdj_element("mjlist")
        if "fs" in form.keys():
            self.swdj_page.send_keys_swdj_element("fs", form.get("fs"), True)
        if "bq" in form.keys():
            self.swdj_page.send_keys_swdj_element("bq", form.get("bq"))

    def fill_dept(self, yysx, **deptInfo):
        if yysx == True:
            self.swdj_page.click_swdj_element("yysx")
            iframe = self.swdj_page.get_swdj_element("iframe")
            self.driver.switch_to.frame(iframe)
            self.swdj_page.click_swdj_element("xzsx")
            self.swdj_page.click_swdj_element("szsxbutton")
            self.driver.switch_to.default_content()
        else:
            pass


    def upload_file(self, file_path):
        self.swdj_page.click_swdj_element("bdsc")
        time.sleep(1)
        UploadFile.upload_one(file_path)

    def save(self):
        self.swdj_page.click_swdj_element("save")

    def send(self):
        self.swdj_page.click_swdj_element("send")

