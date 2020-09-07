#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
class FirstClass01(unittest.TestCase):
    def setUp(self):
        print("qianzhi")
    def tearDown(self):
        print("houzhi")

    def testfirst01(self):
        print("zheshidiyigecase")

    def testfirst02(self):
        print("222222222")

if __name__ == '__main__':
    unittest.main()
