#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import os
class FirstClass01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("souyouqqqq")

    @classmethod
    def tearDownClass(cls):
        print("suoyouhhhh")

    def setUp(self):
        print("qianzhi")

    def tearDown(self):
        print("houzhi")

   # @unittest.skip("buszhixing")
    def testfirst01(self):
        a = False
        self.assertFalse(a, "执行了")
        io.Stri
        print("11")

    def testfirst02(self):
        b = True
        self.assertFalse(b, "执行了")
        print("12")

if __name__ == '__main__':
    #unittest.main()
    file_path = os.path.join(os.getcwd() + r"\report\u_case.html")
    print(file_path)
    f = open(file_path, 'wb')
    suit = unittest.TestSuite()
    suit.addTest(FirstClass01("testfirst01"))
    suit.addTest(FirstClass01("testfirst02"))
    #unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="title", description=u"测试报告", verbosity=2)
    runner.run(suit)
