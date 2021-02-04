#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.swdj_handle import SwdjHandle
from handle.index_handle import IndexHandle

class PtswBuiness(object):
    def __init__(self, driver):
        self.swdj = SwdjHandle(driver)
        self.index = IndexHandle(driver)
        self.driver = driver

    def ptsw_save(self, bt, file_path, **form):
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
        #保存


