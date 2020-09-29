#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
class ScreenShot():
    def __init__(self, driver):
        self.driver = driver
    @classmethod
    def makedir(cls, file_path):
        try:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
                print("新建目录成功")
            else:
                print("目录已存在")
        except BaseException as msg:
            print("新建目录失败: %s" % msg)

    def shot(self):
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        file_path = os.path.join(os.path.dirname(os.getcwd()), "report", directory_time)
        self.makedir(file_path)
        picture_time = time.strftime("%H-%M-%S", time.localtime(time.time()))
        try:
            pic_path = file_path + "\\" + picture_time + ".png"
            self.driver.save_screenshot(pic_path)
            print("截图成功")
        except BaseException as pic_msg:
            print("截图失败:%s" % pic_msg)
