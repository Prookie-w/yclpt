#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from page.login_page import LoginPage
class LoginHandle(object):
    def __init__(self, driver):
        self.login_page = LoginPage(driver)

    def send_username(self, username):
        self.login_page.get_username_element().send_keys(username)

    def send_password(self, password):
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        self.login_page.get_submit_element().click()

    def get_error_info(self):
        text = self.login_page.get_error_element().text

    def get_login_info(self):
        text = self.login_page.get_title_element()
        return text
