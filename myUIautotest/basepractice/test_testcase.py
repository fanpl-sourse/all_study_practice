# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 16:36
# @Author  : 饭盆里
# @File    : test_testcase.py
# @Software: PyCharm
# @desc    : 编写UI自动化测试用例
from time import sleep
from selenium import webdriver

class TestTestcase():
    def setup_class(self):
        print('*'*20+'setupclass'+'*'*20)
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown_class(self):
        print('*'*20+'teardownclass'+'*'*20)
        self.driver.quit()

    def test_case(self):
        self.driver.find_element_by_xpath('//*[@id="main-nav-menu"]/ul/li[4]/a').click()
        sleep(3)
        print('hi')