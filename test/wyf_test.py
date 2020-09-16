#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.browser_driver import BrowserDriver
if __name__ == '__main__':
    #driver_path = r"E:\work\code\tools/driver/home\chromedriver.exe"
    #driver = webdriver.Chrome(driver_path)
    #driver.get("http://www.baidu.com")
    driver = BrowserDriver(object).open_browser("home", "http://172.23.23.223:8080/yclpt")
    driver.maximize_window()


