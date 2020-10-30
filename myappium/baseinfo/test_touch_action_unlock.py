# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 08:59
# @Author  : 饭盆里
# @File    : test_touch_action_unlock.py
# @Software: PyCharm
# @desc    : 手势密码锁
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver


class TestTouchActionUnlock:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_unlock(self):
        TouchAction(self.driver).press(x=120,y=180).wait(100).move_to(x=366,y=180).wait(100).move_to(x=600,y=180).wait(100).\
             move_to(x=600,y=420).wait(100).move_to(x=600,y=660).wait(100).release().perform()
