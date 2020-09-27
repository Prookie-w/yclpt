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
        print("11")

    def testfirst02(self):
        b = True
        self.assertFalse(b, "执行了")
        print("12")

if __name__ == '__main__':
    file_path = os.path.join(r"E:\work\code\report\u_case.html")
    print("aaaaa")
