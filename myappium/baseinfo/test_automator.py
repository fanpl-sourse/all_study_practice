# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 14:34
# @Author  : 饭盆里
# @File    : test_automator.py
# @Software: PyCharm
# @desc    :
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAutomator:
    def setup(self):
        despire_cap = {
            "platformName": "android",
            "deviceName": "emulator-5554",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": 'true',
            "unicodeKeyBord": 'true'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', despire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_automator_xpath(self):
        """
        1. 点击我的，进入个人信息页
        2. 点击登录，进入登录页面
        3. 输入用户名，输入密码
        4. 点击登录
        :return:
        """
        sleep(2)
        self.driver.find_element(MobileBy.XPATH,'//*[@text="我的" and @class="android.widget.TextView"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="帐号密码登录"]').click()
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/login_account').send_keys('18799999999')
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/login_password').send_keys('123456')

        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/button_next').click()
        sleep(2)

    def test_automator_uiautomator(self):
        """
        通过uiautomator的形式进行
        :return:
        """
        sleep(2)
        #点击"我的"
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('18799999999')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')

        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        sleep(3)