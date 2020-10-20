#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from base.browser_driver import BrowserDriver
from business.login_business import LoginBusiness
from lxml.html import etree
import time
from base.find_element import FindElement
from handle.ptsw_handle import PtswHandle
class wyf():

    def info(self, a, *name, **addr):
        print('a is', a)
        for s in name:
            print('name', s)

        for local, floor in addr.items():
            print(local, 'is', floor)

    def css(self):
        test = '''
        <div class="input_wd_1 fd-no-right-border fd-no-left-border fd-no-margin-left fd-no-margin-right aty-form-item aty-form-item-label-right" style="width: 68%;" title="qqqqqqqqq">
<div class="aty-form-item-content" style="margin-left: 130px;">
<div class="aty-input-wrapper aty-input-wrapper-default aty-input-type-text">
<div class="aty-input-box">
<i class="aty-icon aty-icon-load-c aty-load-loop aty-input-icon aty-input-icon-validate"></i> 
<input autocomplete="off" spellcheck="false" placeholder="" maxlength="1000" name="" type="text" class="aty-input aty-input-default"></div> 
</div>
</div>
</div>
            '''
        html = etree.HTML(test)
        a = "input[class$=\'aty-input-default\']:nth-of-type(1)"
        span = html.cssselect(a)
        print(span)

    def css_test(self):
        driver = BrowserDriver(object).open_browser("Chrome", "http://172.23.22.179:8080/yclpt")
        #driver = BrowserDriver(object).open_browser("home", "http://172.23.22.179:8080/yclpt")
        driver.maximize_window()
        LoginBusiness(driver).login_base("songll", "12345678Aa")
        driver.implicitly_wait(10)
        time.sleep(5)
        PtswHandle(driver).click_ptsw()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        print(driver.title)
        #msg = FindElement(driver, "IndexElement").get_element("ptsw_button").get_attribute("type")
        msg = FindElement(driver, "SwdjElement").get_element("bt")
        #.get_attribute("type")
        print(msg)




if __name__ == '__main__':
    #wyf().info(10, 1, 2, 3, 4, 5, heida=31, suning=22, huayu=77)
    wyf().css_test()
    #wyf().css()




