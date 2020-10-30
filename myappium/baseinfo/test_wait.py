# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 17:53
# @Author  : 饭盆里
# @File    : test_wait.py
# @Software: PyCharm
# @desc    :   appium中wait的使用
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #隐式等待默认都加，在服务端的等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_sleep(self):
        #强制等待，一般不推荐
        sleep(2)

    def test_WebDriverWait(self):
        locator = (MobileBy.ID,'com.xueqiu.android:id/tv_search')
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))
        print('hi')