#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
class FirstCase(unittest.TestCase):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("httPxx")
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        self.driver.close()
        print("houzhi")

    def test_login_password_error(self):
        password_error = self.login.login_password_error("34", "111")
        self.assertFalse(password_error, "成功")
        if password_error == True:
            print("登录成功")
        
    def test_login_username_error(self):
        username_error = self.login.login_username_error("34", "111")
        if username_error == True:
            print("登录成功")

    def test_login_success(self):
        success = self.login.login_success("34", "111")
        if success == True:
            print("登录成功")

def  main():
    first = FirstCase()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()


if __name__ == '__main__':
    unittest.main()