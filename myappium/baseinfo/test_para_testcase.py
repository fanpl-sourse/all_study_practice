# -*- coding: utf-8 -*-
# @Time    : 2020/10/31 12:07
# @Author  : 饭盆里
# @File    : test_para_testcase.py
# @Software: PyCharm
# @desc    : 参数化测试用例
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestXueqiuSearch:
    def setup(self):
        desire_cap= {
        "platformName": "android",
        "deviceName": "emulator-5554",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "noReset":"true",
        "unicodeKeyBord":"true",
        "skipDeviceInitialization":"true",
        "resetKeyboard":"true"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        # self.driver.quit()

    @pytest.mark.parametrize(('send_key,title,price'),[
        ('阿里巴巴','阿里巴巴',300),
        ('京东', '京东', 80),
    ],ids=['alibaba','JD'])
    def test_search(self,send_key,title,price):
        """
        1.打开雪球APP
        2.点击搜索输入框
        3.在搜索框输入"阿里巴巴"
        4.在搜索结果中选择 "阿里巴巴"，然后点击
        5.获取阿里巴巴股价，并判断价格>300
        :return:
        """
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys(send_key)
        self.driver.find_element(MobileBy.XPATH,f'//*[@class="android.widget.TextView" and @text="{send_key}"]').click()
        current_price = float(self.driver.find_element(MobileBy.XPATH,f'//*[@class="android.widget.TextView" and @text="{title}"]/../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text)

        assert_that(current_price,close_to(price,price*0.5))