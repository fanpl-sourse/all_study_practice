# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:16
# @Author  : 饭盆里
# @File    : app.py
# @Software: PyCharm
# @desc    :
from appium import webdriver
from myappium.xueqiu.page.basepage import BasePage
from myappium.xueqiu.page.main_page import MainPage
from myappium.xueqiu.tools.readyaml import Tools


class App(BasePage):
    """
    APP的基本操作，打开APP，关闭APP，进入主页面
    """

    caps_data = Tools().read_yaml('../setting.yaml')['caps']

    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"

    def start(self):
        """
        启动APP
        :return:
        """
        if self.driver == None:
            # despire_cap = {
            #     "platformName": "android",
            #     "deviceName": "emulator-5554",
            #     "appPackage": self._appPackage,
            #     "appActivity": self._appActivity,
            #     "noReset": 'true',
            #     "unicodeKeyBord": 'true'
            # }

            despire_cap = {
                "platformName": self.caps_data['platformName'],
                "deviceName": self.caps_data['deviceName'],
                "appPackage": self._appPackage,
                "appActivity": self._appActivity,
                "noReset": self.caps_data['noReset'],
                "unicodeKeyBord": self.caps_data['unicodeKeyBord']
            }

            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', despire_cap)
        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # self.driver.launch_app()
            self.driver.start_activity(self._appPackage,self._appActivity)

        self.driver.implicitly_wait(10)
        return self

    def stop(self):
        """
        关闭APP
        :return:
        """
        self.driver.quit()

    def goto_mainpage(self):
        """
        进入主页面
        :return:
        """
        return MainPage(self.driver)