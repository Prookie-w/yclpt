#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import unittest
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
from unit.screenshot import ScreenShot
from business.ptsw_buiness import PtswBuiness
import os
import HTMLTestRunner
import time
import random


class PtswCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = BrowserDriver(object).open_browser("Chrome", "http://172.23.23.223:8080/yclpt")
        self.driver.maximize_window()
        self.login = LoginBusiness(self.driver)
        self.ptsw = PtswBuiness(self.driver)
        self.login.login_base("songll", "12345678Aa")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = str(method_name).split("(")[0]
                ScreenShot(self.driver).shot(case_name)
        #self.driver.close()

    def test_ptsw_save(self):
        bt = "savetest" + str(random.randint(0, 999))
        lwhm = time.strftime("%m%d%H%M%S", time.localtime()) + "号"
        file_path = "C:\\Users\\huayu\\Desktop\\nmon16e_mpginc.tar.gz"
        #file_path = "D:\\baiduNetDiskDownload\\test.txt"
        action = "save"
        self.ptsw.ptsw_save(bt, file_path, action, lwdw="上海", lwh="沪", lwhm=lwhm, btlx='nbd', fs="20", bq="标签")
        result = self.ptsw.check(bt, "nbd")
        self.assertTrue(result, "收文单新建失败")

    def ptsw_send(self):
        bt = "sendtest" + str(random.randint(0, 999))
        lwhm = time.strftime("%m%d%H%M%S", time.localtime()) + "号"
        file_path = "C:\\Users\\huayu\\Desktop\\nmon16e_mpginc.tar.gz"
        #file_path = "D:\\baiduNetDiskDownload\\test.txt"
        action = "send"
        self.ptsw.ptsw_save(bt, file_path, action, lwdw="上海", lwh="沪", lwhm=lwhm, btlx='psj', fs="20", bq="标签")


if __name__ == '__main__':
    report_path = os.path.join(os.path.dirname(os.getcwd()), "report", "u_case.html")
    f = open(report_path, 'wb')
    suit = unittest.TestSuite()
    suit.addTest(PtswCase("test_ptsw_save"))
    # suit.addTest(PtswCase("test_ptsw_send"))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description=u"预处理的测试报告", verbosity=2)
    runner.run(suit)

