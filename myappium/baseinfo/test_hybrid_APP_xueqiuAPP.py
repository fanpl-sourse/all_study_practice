# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 10:09
# @Author  : 饭盆里
# @File    : test_hybrid_APP_xueqiuAPP.py
# @Software: PyCharm
# @desc    :
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestHybridAppXueqiuapp:
    def setup(self):
        desire_cap={
            "platformName": "android",
            "platformVersion": "6.0",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "deviceName": "emulator-5554",
            "noReset": True
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_cap)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def  test_hybrid_app_xueqiuapp(self):
        """
        打开应用
        点击‘交易’
        点击‘A股开户’
        再输入用户名和密码
        点击‘立即开户’
        退出应用
        :return:
        """

        print(self.driver.contexts)
        #点击交易
        self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.TextView" and @text="交易"]').click()
        print(self.driver.contexts)
        sleep(2)

