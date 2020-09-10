#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
class FirstClass02(unittest.TestCase):
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

    def testfirst21(self):
        print("21")

    def testfirst22(self):
        print("22")

if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(FirstClass02("testfirst21"))
    suit.addTest(FirstClass02("testfirst22"))
    unittest.TextTestRunner().run(suit)
