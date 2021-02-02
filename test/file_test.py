#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
import time
from base.find_element import FindElement
from handle.swdj_handle import PtswHandle
from unit.upload_file import UploadFile


class FileTest(object):

    def test(self):
        driver = BrowserDriver(object).open_browser("Chrome", "http://172.23.22.179:8080/yclpt")
        driver.maximize_window()
        LoginBusiness(driver).login_base("songll", "12345678Aa")
        driver.implicitly_wait(10)
        PtswHandle(driver).click_ptsw()
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        js = 'swdjVo.cbt=1231321'
        driver.execute_script(js)
        time.sleep(2)
        FindElement(driver, "SwdjElement").get_element("bt").send_keys("zxcvzxvzxcvxzv")
        FindElement(driver, "SwdjElement").get_element("swh").click()
        time.sleep(1)
        FindElement(driver, "SwdjElement").get_element("swhlist").click()
        #msg = driver.find_element_by_css_selector(".aty-btn.aty-btn-ghost.aty-btn-icon-only").click()
        #print(msg)
        FindElement(driver, "SwdjElement").get_element("bdsc").click()
        time.sleep(1)
        UploadFile.upload_one('C:\\Users\\huayu\\Desktop\\bigdata_stdout.log')
        time.sleep(5)


if __name__ == '__main__':
    FileTest().test()
