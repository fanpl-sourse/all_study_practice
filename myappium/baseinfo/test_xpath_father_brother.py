# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 11:45
# @Author  : 饭盆里
# @File    : test_xpath_father_brother.py
# @Software: PyCharm
# @desc    : 通过父子节点定位的方式找到元素
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXpath:
    def setup(self):
        despire_cap={
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": 'true',
            "unicodeKeyBord": 'true'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',despire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_xpath(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        self.driver.find_element(MobileBy.XPATH,'//*[@text="BABA"]').click()
        element =self.driver.find_element(MobileBy.XPATH,'//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        assert float(element.get_attribute('text')) >200