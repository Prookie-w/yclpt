#!/usr/bin/env python
# -*- coding:utf-8 -*-
import ddt
import unittest
@ddt.ddt
class DateTest(unittest.TestCase):
    def setUp(self):
        print("setup")
    def tearDown(cls):
        print("tearDown")

    @ddt.data(
        [1, 2],
        [3, 4],
        [5, 6]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a+b)

if __name__ == '__main__':
    unittest.main()