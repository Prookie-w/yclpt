#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from page.login import LoginPage
class LoginHandle(object):
    def __init__(self, driver):
        self.login_p = LoginPage(driver)

    def send_username(self, username):
        self.login_p.get_username_element().send_keys(username)

    def send_password(self, password):
        self.login_p.get_password_element().send_keys(password)

    def click_login(self):
        pass

    def get_error_info(self):
        self.login_p.get_error_text()
