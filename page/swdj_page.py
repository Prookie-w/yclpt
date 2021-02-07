#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.find_element import FindElement


class SwdjPage(object):
    def __init__(self, driver):
        self.find_e = FindElement(driver, "SwdjElement")

    def get_swh_element(self):
        return self.find_e.get_element("swh")

    def get_bt_element(self):
        return self.find_e.get_element("bt")

    def get_swhlist_element(self):
        return self.find_e.get_element("swhlist")

    def get_lwdw_element(self):
        return self.find_e.get_element("lwdw")

    def get_lwdwlist_element(self):
        return self.find_e.get_element("lwdwlist")

    def get_lwh_element(self):
        return self.find_e.get_element("lwh")

    def get_lwhlist_element(self):
        return self.find_e.get_element("lwhlist")

    def get_bdsc_element(self):
        return self.find_e.get_element("bdsc")

    def get_lwhm_element(self):
        return self.find_e.get_element("lwhm")

    def get_psj_element(self):
        return self.find_e.get_element("psj")

    def get_nbd_element(self):
        return self.find_e.get_element("nbd")

    def get_mj_element(self):
        return self.find_e.get_element("mj")

    def get_mjlist_element(self):
        return self.find_e.get_element("mjlist")

    def get_fs_element(self):
        return self.find_e.get_element("fs")

    def get_bq_element(self):
        return self.find_e.get_element("bq")

    def get_yysx_element(self):
        return self.find_e.get_element("yysx")

    def get_iframe_element(self):
        return self.find_e.get_element("iframe")

    def get_xzsx_elemenet(self):
        return self.find_e.get_element("xzsx")

    def get_szsxbutton_element(self):
        return self.find_e.get_element("szsxbutton")

    def get_swdj_element(self, ele):
        return self.find_e.get_element(ele)

    def click_swdj_element(self, ele):
        self.find_e.get_element(ele).click()

    def send_keys_swdj_element(self, ele, text, clear=True):
        if clear:
            self.find_e.get_element(ele).send_keys(text)
        else:
            e = self.find_e.get_element(ele)
            e.clear()
            e.send_keys(text)
