# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 09:26
# @Author  : 饭盆里
# @File    : test_Hybrid_APP_APPdemo.py
# @Software: PyCharm
# @desc    : 用Appdemo测试 混合应用
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestHybridAppdemo:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "platformVersion":"6.0",
            "appPackage": "io.appium.android.apis",
            "appActivity": ".ApiDemos",
            "deviceName": "emulator-5554",
            "noReset":True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hybrid_appdemo(self):
        """
        1. 打开appdemo APP
        2. 找到View，点击
        3. 滚动查找到WebView，点击
        4. 跳转到webview页面，  注意：需要从原生切换到webview
        5. 然后在webview页面进行一系列操作：输入框输入值、点击链接等
        :return:
        """
        # print(self.driver.contexts)
        self.driver.find_element_by_accessibility_id('Views').click()
        #滚动查找到元素
        scroll_to_find_webview = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0))'
        self.driver.find_element_by_android_uiautomator(scroll_to_find_webview).click()

        #从原生切换到webview,切换目录？？
        # print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])

        #下面就要用本地浏览器进行映射定位了
        self.driver.find_element(By.ID,'i_am_a_textbox').send_keys('hello,nob')
        self.driver.find_element(By.ID,'i am a link').click()
        sleep(2)

