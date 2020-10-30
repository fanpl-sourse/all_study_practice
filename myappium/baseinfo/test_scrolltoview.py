# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 21:36
# @Author  : 饭盆里
# @File    : test_scrolltoview.py
# @Software: PyCharm
# @desc    : 滚动直到看到元素
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestScrolltoview:
    def setup(self):
        despire_cap={
          "platformName": "android",
          "deviceName": "emulator-5554",
          "appPackage": "com.xueqiu.android",
          "appActivity": ".view.WelcomeActivityAlias"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',despire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_scrolltoview(self):
        """
        1. 打开雪球APP
        2. 首页-点击关注
        3. 在关注列表中滚动查找某个文本信息
        :return:
        """
        self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.TextView" and @text="关注"]').click()

        uiautomator_element1 = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("-老榕树-").instance(0))'
        self.driver.find_element_by_android_uiautomator(uiautomator_element1).click()



