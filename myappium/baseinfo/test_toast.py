# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 22:30
# @Author  : 饭盆里
# @File    : test_toast.py
# @Software: PyCharm
# @desc    : 练习toast弹框的捕获
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        despire_cap={
          "platformName": "android",
          "deviceName": "emulator-5554",
          "appPackage": "io.appium.android.apis",
          "appActivity": "io.appium.android.apis.view.PopupMenu1"
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',despire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Search"]').click()
        #获取当前页面的dom结构
        # print(self.driver.page_source)
        #根据xpath中class 定位，因为一个页面的弹框一般只有一个，输出弹框内容
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        #根据文本信息，输出弹框内容
        print(self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"Clicked popup")]').text)