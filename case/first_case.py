#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from business.register_business import RegisterBusiness
class FirstCase(object):
    def __init__(self):
        self.login = RegisterBusiness()

    def test_login_password_error(self):
        self.login.login("34", "111")
        
    def test_login_username_error(self):
        self.login.login("34", "111")

    def test_login_success(self):
        self.login.login("34", "111")
