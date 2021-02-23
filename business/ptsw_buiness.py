#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.swdj_handle import SwdjHandle
from handle.index_handle import IndexHandle
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PtswBuiness(object):
    def __init__(self, driver):
        self.swdj = SwdjHandle(driver)
        self.index = IndexHandle(driver)
        self.driver = driver

    def ptsw_save(self, bt, file_path, action, **form):
        #点击普通收文
        self.index.click_ptsw()
        #切换窗口
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        #填写收文单
        self.swdj.fill_in_form(bt, **form)
        #填写处室信息
        self.swdj.fill_dept(True)
        #上传附件
        self.swdj.upload_file(file_path)
        if action == "save":
            self.swdj.save()
        elif action == "send":
            self.swdj.send()
        self.driver.switch_to.window(windows[0])

    def test(self):
        return False

    def cgx(self):
        self.index.click_lwycl()
        #locator = (By.CLASS_NAME, "aty-tabs-tab")
        #WebDriverWait(self.driver, 10, 2).until(EC.presence_of_element_located(locator))
        time.sleep(1)
        self.index.click_cgx()
        time.sleep(1)





