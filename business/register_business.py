#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.register_handle import LoginHandle
class RegisterBusiness(object):
    def __init__(self, driver):
        self.login = LoginHandle(driver)
    #执行操作
    def login(self, username, password):
        self.login.send_username(username)
        self.login.send_password(password)
        self.login.click_login()
        if self.login.get_error_info():
            return True
