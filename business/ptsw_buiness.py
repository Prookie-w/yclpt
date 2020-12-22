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
        self.ptsw.click_ptsw()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.ptsw.fill_in_form(bt, **form)
        self.ptsw.upload_file(file_path)


