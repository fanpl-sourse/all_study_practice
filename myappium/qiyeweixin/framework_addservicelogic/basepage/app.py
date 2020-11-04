# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:14
# @Author  : 饭盆里
# @File    : app.py
# @Software: PyCharm
# @desc    :
from appium import webdriver
from myappium.qiyeweixin.framework_addservicelogic.pages.main_page import MainPage

class App:
    """
    APP相关动作
    """
    def start(self):
        """
        启动APP
        :return:
        """
        desire_caps = {
            "platformName": "android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "deviceName": "emulator-5554",
            "noReset": "true",
            'skipServerInstallation': 'true',  # 跳过 uiautomator2 server的安装
            'skipDeviceInitialization': 'true',  # 跳过设备初始化
            'settings[waitForIdleTimeout]': 0,  # 等待Idle为0
            'dontStopAppOnReset': 'true'  # 不关闭，重启APP
        }

        # 与server建立连接，初始化一个driver，创建session
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(5)

        return MainPage(self.driver)

    def restart(self):
        """
        重启APP
        :return:
        """
        return MainPage()

    def stop(self):
        """
        停止APP
        :return:
        """
        self.driver.quit()