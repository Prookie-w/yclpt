#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = BrowserDriver(object).open_browser("home", "http://172.23.23.223:8080/yclpt")
        self.driver.maximize_window()
        self.login = LoginBusiness(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_login_username_error(self):
        password_error = self.login.login_username_error("aaa", "123456Aa")
        self.assertFalse(password_error, "成功")
        if password_error == True:
            print("登录成功")

if __name__ == '__main__':
    #suit = unittest.TestSuite()
    #suit.addTest()
    unittest.main()
