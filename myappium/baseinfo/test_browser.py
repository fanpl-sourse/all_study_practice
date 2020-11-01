# -*- coding: utf-8 -*-
# @Time    : 2020/10/31 15:13
# @Author  : 饭盆里
# @File    : test_browser.py
# @Software: PyCharm
# @desc    : 测试浏览器页面
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestChrome:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "platformVersion":"6.0",
            "deviceName": "emulator-5554",
            "browserName":"Browser",
            "noReset":True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_browser_baidu(self):
        """
        打开百度页面
        :return:
        """
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID,"kw").send_keys('selenium')
        self.driver.find_element(By.ID,"su").click()
        sleep(2)