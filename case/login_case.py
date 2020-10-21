#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
import os
import HTMLTestRunner
from unit.screenshot import ScreenShot
class LoginCase(unittest.TestCase):

    def setUp(self):
        self.driver = BrowserDriver(object).open_browser("Chrome", "http://172.23.23.223:8080/yclpt")
        self.driver.maximize_window()
        self.login = LoginBusiness(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = str(method_name).split("(")[0]
                ScreenShot(self.driver).shot(case_name)
        self.driver.close()

    def test_login_username_error(self):
        username_error = self.login.login_username_error("aaa", "123456Aa")
        self.assertTrue(username_error, "用例执行失败")

    def test_login_password_error(self):
        password_error = self.login.login_password_error("wangq", "123456789")
        self.assertTrue(password_error, "用例执行失败")

    def test_login_success(self):
        message = self.login.login_success("songll", "12345678Aa")
        self.assertTrue(message, "用例执行失败")

if __name__ == '__main__':
    report_path = os.path.join(os.path.dirname(os.getcwd()), "report", "u_case.html")
    f = open(report_path, 'wb')
    suit = unittest.TestSuite()
    suit.addTest(LoginCase("test_login_username_error"))
    suit.addTest(LoginCase("test_login_password_error"))
    suit.addTest(LoginCase("test_login_success"))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description=u"预处理的测试报告", verbosity=2)
    runner.run(suit)
