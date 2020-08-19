from selenium import webdriver
import time
import os
dir = os.path.dirname(os.path.abspath('.'))
chrome_driver_path = dir + r'\yclpt\tools\360de78\chromedriver.exe'
print(chrome_driver_path)
_browser_url = r'F:\Program Files (x86)\360liulanqi\360se6\Application\360se.exe'
options = webdriver.ChromeOptions()
options.binary_location = _browser_url
driver = webdriver.Chrome(
    options=options,
    executable_path=chrome_driver_path)
driver.maximize_window()
driver.get("http://172.23.23.223:8080/yclpt/")
time.sleep(3)
driver.quit()
