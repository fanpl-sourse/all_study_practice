# -*- coding: utf-8 -*-
# @Time : 2020/7/23 16:28
# @Author : 饭盆里
# @File : test_xueqiu_search.py
# @Software: PyCharm
# @desc :
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestXueqiuSearch:
    def setup(self):
        desire_cap= {
        "platformName": "android",
        "deviceName": "emulator-5554",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "dontStopAppOnReset":'true',
        "noReset":'true',
        "unicodeKeyBord":'true'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()
        self.driver.quit()

    def test_search(self):
        """
        1.打开雪球APP
        2.点击搜索输入框
        3.在搜索框输入"阿里巴巴"
        4.在搜索结果中选择 "阿里巴巴"，然后点击
        5.获取阿里巴巴股价，并判断价格>200
        :return:
        """
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.TextView" and @text="阿里巴巴"]').click()
        current_price = float(self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.TextView" and @text="阿里巴巴"]/../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)

        # current_price = float(self.driver.find_element(MobileBy.XPATH,'//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)
        assert current_price>200
