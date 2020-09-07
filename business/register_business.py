#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.register_handle import LoginHandle
class RegisterBusiness(object):
    def __init__(self, driver):
        self.login = LoginHandle(driver)

    def login_base(self, username, password):
        self.login.send_username(username)
        self.login.send_password(password)
        self.login.click_login()

    #执行操作
    def login_username_error(self, username, password):
        self.login_base(username, password)
        if self.login.get_error_info() == "用户名错误":
            print("用户名错误")
            return True
        else:
            return False

    def login_password_error(self, username, password):
        self.login_base(username, password)
        if self.login.get_error_info() == "密码错误":
            print("密码错误")
            return True
        else:
            return False

    def login_success(self, username, password):
        self.login_base(username, password)
        if self.login.get_login_info() == "预处理平台":
            print("登录成功")
            return True
        else:
            return False
