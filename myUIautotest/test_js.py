# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 10:00
# @Author  : 饭盆里
# @File    : test_js.py
# @Software: PyCharm
# @desc    : js相关操作
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestJs():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()

    def test_js_scroll(self):
        self.driver.get('https://www.baidu.com/')
        searchelement = self.driver.find_element(By.ID,'kw')
        searchelement.send_keys('selenium官网')
        self.driver.find_element(By.ID,'su').click()
        sleep(2)

        """
        # 功能同js
        action = TouchActions(self.driver)
        action.scroll_from_element(searchelement,0,10000)
        action.perform()
        sleep(2)
        """
        js = 'document.documentElement.scroll=10000'
        self.driver.execute_script(js)

        self.driver.find_element(By.XPATH,'//*[@id="page"]//a[last()]').click()
        sleep(2)

    def test_js_time(self):
        """
        对时间控件进行赋值
        :return:
        """
        self.driver.get('https://www.12306.cn/index/')
        sleep(2)
        js = 'a = document.getElementById("train_date"), a.value = "2020-10-06"'

        self.driver.execute_script(js)

        sleep(2)

