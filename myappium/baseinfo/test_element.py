# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 22:24
# @Author  : 饭盆里
# @File    : test_element.py
# @Software: PyCharm
# @desc    : 元素常用属性 常用方法实战
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueqiuSearch():
    def setup(self):
        desire_cap= {
        "platformName": "android",
        "deviceName": "emulator-5554",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "noReset":'true',
        "unicodeKeyBord":'true'
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
            self.driver.back()
            self.driver.quit()

    def test_attribute(self):
        """
        1. 打开【xueqiu】首页
        2. 定位首页搜索框
        3. 判断搜索框是否可用，并查看搜索框name属性值
        4. 打印搜索这个元素的坐标和宽高
        5. 在搜索框输入：阿里巴巴
        6. 判断阿里巴巴是否可见
        7. 如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”
        :return:
        """
        search_element = self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search')
        print(search_element.get_attribute('clickable'))
        print(search_element.get_attribute('name'))
        print(search_element.location)
        print(search_element.size)
        search_element.click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        print(self.driver.find_element(MobileBy.XPATH,'//*[@text="BK0515"]').get_attribute('clickable'))


    def test_attr(self):
        """
        1. 打开【xueqiu】首页
        2. 定位首页搜索框
        3. 判断搜索框是否可用，并查看搜索框name属性值
        4. 打印搜索这个元素的坐标和宽高
        5. 在搜索框输入：阿里巴巴
        6. 判断阿里巴巴是否可见
        7. 如果可见，打印“搜索成功”，如果不可见，打印“搜索失败”
        :return:
        """
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        if element.is_enabled() == True:
            print(element.text)
            print(element.location)
            # print(element.tag_name)
            print(element.size)
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            element = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        if element.is_displayed() == True:
            print("搜索成功")
        else:
            print("搜索失败")


