from selenium import webdriver
import time
import random
#from PIL import Image
#from ShowapiRequest import ShowapiRequest
from base.find_element import FindElement
class RegisterFunction(object):
    def __init__(self, url):
        self.driver =self.get_driver(url)

    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
    def get_rande_user(self):
        pass
    def get_code_image(self, file_name):
        pass
