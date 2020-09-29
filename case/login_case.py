#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
import os
import HTMLTestRunner
from unit.screenshot import ScreenShot
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = BrowserDriver(object).open_browser("home", "http://172.23.23.223:8080/yclpt")
        self.driver.maximize_window()
        self.login = LoginBusiness(self.driver)

    @classmethod
    def tearDownClass(self):
        ScreenShot(self.driver).shot()
        self.driver.close()

    def test_login_username_error(self):
        password_error = self.login.login_username_error("aaa", "123456Aa")
        self.assertFalse(password_error, "成功")

if __name__ == '__main__':
    report_path = os.path.join(os.path.dirname(os.getcwd()), "report", "u_case.html")
    f = open(report_path, 'wb')
    suit = unittest.TestSuite()
    suit.addTest(LoginCase("test_login_username_error"))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description=u"预处理的测试报告", verbosity=2)
    runner.run(suit)
