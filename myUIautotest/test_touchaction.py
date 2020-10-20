# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 17:33
# @Author  : 饭盆里
# @File    : test_touchaction.py
# @Software: PyCharm
# @desc    : touchaction操作
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchaction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()

    def test_touchactions_scroll(self):
        self.driver.get('https://www.baidu.com/')
        searchelement = self.driver.find_element(By.ID,'kw')
        searchelement.send_keys('selenium官网')
        self.driver.find_element(By.ID,'su').click()
        sleep(2)

        action = TouchActions(self.driver)
        action.scroll_from_element(searchelement,0,10000)
        sleep(2)
        action.perform()