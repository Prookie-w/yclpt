#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
from unit.screenshot import ScreenShot
from  business.ptsw_buiness import PtswBuiness


class ptswCase(unittest.TestCase):
    def setUpClass(cls):
        cls.driver = BrowserDriver(object).open_browser("Chrome", "http://172.23.23.223:8080/yclpt")
        cls.driver.maximize_window()
        cls.login = LoginBusiness(cls.driver)
        cls.ptsw = PtswBuiness(cls.driver)
        cls.login.login_base("songll", "12345678Aa")

    def tearDownClass(cls):
        cls.driver.close()

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = str(method_name).split("(")[0]
                ScreenShot(self.driver).shot(case_name)

    def test_ptsw_save(self):
        self.ptsw.ptsw_save()


