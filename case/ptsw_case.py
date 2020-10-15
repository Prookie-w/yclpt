#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
class ptswCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserDriver(object).open_browser("Chrome", "http://172.23.23.223:8080/yclpt")
        cls.driver.maximize_window()
        cls.login = LoginBusiness(cls.driver)
        cls.login.login_base("songll", "12345678Aa")

    def tearDownClass(cls):
        pass

    def test_save_swd(self):
        pass

