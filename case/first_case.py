#!/usr/bin/env python 
# -*- coding:utf-8 -*-
class FirstCase(object):
    def test_login_passwd_error(self):
        login("34", "111")

    def test_login_username_error(self):
        login("34", "111")

    def test_login_success(self):
        login("34", "111")