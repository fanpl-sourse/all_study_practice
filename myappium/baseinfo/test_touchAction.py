# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 08:28
# @Author  : 饭盆里
# @File    : test_touchAction.py
# @Software: PyCharm
# @desc    :  touchaction 操作
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_unlock(self):
        """
        手势密码锁
        :return:
        """

    def test_touch_action(self):
        """
        1.打开雪球APP
        2. 在首页滑动(下拉划框)
        :return:
        """
        sleep(3)
        TouchAction(self.driver).press(x=317,y=1084).wait(200).move_to(x=317,y=260).release().perform()
        sleep(3)

    def test_touch_action1(self):
        sleep(3)
        action = TouchAction(self.driver)
        # 获取窗口尺寸
        window_rect = self.driver.get_window_rect()
        x = int(window_rect['width']/2)
        y_start = int(window_rect['height']*0.2)
        y_end = int(window_rect['height']*0.8)
        action.press(x=x,y=y_start).wait(2000).move_to(x=x,y=y_end).release().perform()
        sleep(10)
