# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 09:16
# @Author  : 饭盆里
# @File    : test_chrome.py
# @Software: PyCharm
# @desc    : 多浏览器
import os
from time import sleep
from selenium import webdriver


class Test_chrome():
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('https://www.baidu.com/')
        sleep(2)