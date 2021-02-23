#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
import os
class BrowserDriver():
    dir = os.path.join(os.path.dirname(os.getcwd()), "tools", "driver")
    Chrome_driver_path = os.path.join(dir, "chromedriver.exe")
    IE_driver_path = os.path.join(dir, "IEDriverServer.exe")
    Firfox_driver_path = os.path.join(dir, "geckodriver.exe")
    safe360_driver_path = os.path.join(dir, "360", "chromedriver.exe")
    home_driver_path = os.path.join(dir, "home", "chromedriver.exe")

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, browserType, url):
        if browserType == "Chrome":
            self.driver = webdriver.Chrome(self.Chrome_driver_path)
        elif browserType == "IE":
            self.driver = webdriver.Ie(self.IE_driver_path)
        elif browserType == "FireFox":
            self.driver = webdriver.Firefox(self.Firfox_driver_path)
        elif browserType == "360":
            _brower_url = r"F:\Program Files (x86)\360liulanqi\360se6\Application\360se.exe"
            option = webdriver.ChromeOptions()
            option.binary_location = _brower_url
            self.driver = webdriver.Chrome(options=option, executable_path=option.binary_location)
        elif browserType == "home":
            self.driver = webdriver.Chrome(self.home_driver_path)
        else:
            print("参数错误")
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver
