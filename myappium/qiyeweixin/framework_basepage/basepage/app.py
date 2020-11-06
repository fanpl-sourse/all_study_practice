# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:14
# @Author  : 饭盆里
# @File    : app.py
# @Software: PyCharm
# @desc    :
from appium import webdriver
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.main_page import MainPage

class App(BasePage):
    """
    APP相关动作,比如启动app,关闭APP 停止APP，进入首页
    """
    def start(self):
        """
        启动APP
        :return:
        """
        if  self.driver == None:
            #第一次调用start()方法时，driver为None
            desire_caps = {
                "platformName": "android",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "deviceName": "emulator-5554",
                "noReset": "true",
                'skipServerInstallation': 'true',  # 跳过 uiautomator2 server的安装
                'skipDeviceInitialization': 'true',  # 跳过设备初始化
                'settings[waitForIdleTimeout]': 0,  # 等待Idle为0
                'dontStopAppOnReset': 'true'  # 不关闭，重启APP，首次启动后不再重启
            }

            # 与server建立连接，初始化一个driver，创建session
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        else:
            #launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # start_activity(packagename, activityname) 可以启动其它的应用的页面
            self.driver.launch_app()

        self.driver.implicitly_wait(10)

        return self

    def restart(self):
        """
        重启APP
        :return:
        """
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        """
        停止APP
        :return:
        """
        self.driver.quit()

    def goto_main(self):
        """
        进入主页面
        :return:
        """
        return MainPage(self.driver)