#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.find_element import FindElement


class LoginPage(object):
    def __init__(self, driver):
        self.find_e = FindElement(driver, "LoginElement")

    def get_username_element(self):
        return self.find_e.get_element("username")

    def get_password_element(self):
        return self.find_e.get_element("password")

    def get_submit_element(self):
        return self.find_e.get_element("submit_button")

    def get_error_element(self):
        return self.find_e.get_element("error_text")
