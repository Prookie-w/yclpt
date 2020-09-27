#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner
class FirstClass02(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("111")

    @classmethod
    def tearDownClass(cls):
        print("3333")

    def test_aa(self):
        a = False
        print("222")
        self.assertFalse(a, "执行了")

if __name__ == '__main__':
    file_path = os.path.join(r"E:\work\code\report\u_case.html")
    print(file_path)
    f = open(file_path, 'wb')
    suit = unittest.TestSuite()
    # suit.addTest(FirstClass01("testfirst01"))
    suit.addTest(FirstClass02("test_aa"))
    # unittest.TextTestRunner().run(suit)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="title", description=u"测试报告", verbosity=2)
    runner.run(suit)
