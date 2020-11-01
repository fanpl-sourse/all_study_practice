# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 12:01
# @Author  : 饭盆里
# @File    : test_devices_api.py
# @Software: PyCharm
# @desc    : 设备交互，注意要用sdk自带的embulator 模拟器来运行
from time import sleep
from appium import webdriver


class TestDevicesAPI:
    def setup(self):
        desire_cap={
          "platformName": "android",
          "deviceName": "emulator-5554",
          "appActivity": ".view.WelcomeActivityAlias",
          "appPackage": "com.xueqiu.android"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_devices_api(self):
        pass
        #模拟打电话
        self.driver.make_gsm_call('18700000000','GsmCallActions.CALL')
        #模拟短信
        self.driver.send_sms('18700000001','只有无限接近死亡，才能领悟到生命的真谛')

        self.driver.set_network_connection(2)
        #截屏
        self.driver.get_screenshot_as_file('./photoo/1.png')
        sleep(2)
        self.driver.set_network_connection(4)
        self.driver.get_screenshot_as_file('./photoo/2.png')

        sleep(2)