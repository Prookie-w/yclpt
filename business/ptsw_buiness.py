#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.ptsw_handle import PtswHandle
from unit.upload_file import UploadFile
import time

class PtswBuiness(object):
    def __init__(self, driver):
        self.ptsw = PtswHandle(driver)
        self.driver = driver

    def ptsw_save(self, bt, file_path, **form):
        #点击普通收文
        self.ptsw.click_ptsw()
        #切换窗口
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        #填写收文单
        self.ptsw.fill_in_form(bt, **form)
        #上传附件
        self.ptsw.upload_file(file_path)
        #保存


