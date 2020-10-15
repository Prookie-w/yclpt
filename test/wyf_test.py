#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.find_element import FindElement
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
import time
class wyf():

    def info(self, a, *name, **addr):
        print('a is', a)
        for s in name:
            print('name', s)

        for local, floor in addr.items():
            print(local, 'is', floor)

    def css_test(self):
        driver = BrowserDriver(object).open_browser("home", "http://172.23.23.223:8080/yclpt")
        driver.maximize_window()
        LoginBusiness(driver).login_base("songll", "12345678Aa")
        time.sleep(5)
        msg = FindElement(driver, "zzlwElement").get_element("ptsw_button").get_attribute("type")
        print(msg)


if __name__ == '__main__':
    #wyf().info(10, 1, 2, 3, 4, 5, heida=31, suning=22, huayu=77)
    wyf().css_test()



