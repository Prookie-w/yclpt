#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.swdj_handle import SwdjHandle
from handle.index_handle import IndexHandle
import time

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
            time.sleep(5)
        self.driver.switch_to.window(windows[0])

    def cgx(self):
        self.index.click_lwycl()
        time.sleep(3)
        self.index.click_cgx()
        time.sleep(3)



