#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from handle.login_handle import LoginHandle
class LoginBusiness(object):
    def __init__(self, driver):
        self.login = LoginHandle(driver)

    def login_base(self, username, password):
        self.login.send_username(username)
        self.login.send_password(password)
        self.login.click_login()

    #执行操作
    def login_username_error(self, username, password):
        self.login_base(username, password)
        if self.login.get_error_info() == "您输入的用户名或密码错误，请重新输入。":
            print("用户名错误")
            return False
        else:
            return True

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