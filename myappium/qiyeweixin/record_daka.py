# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 18:37
# @Author  : 饭盆里
# @File    : record_daka.py
# @Software: PyCharm
# @desc    : 录制后进行优化，pytest化，增加caps参数，提高测试效率
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestRecordDaka:
    def setup(self):
        desire_caps ={
            "platformName": "android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "deviceName": "emulator-5554",
            "noReset": "true",
            'skipServerInstallation':'true',  # 跳过 uiautomator2 server的安装
            'skipDeviceInitialization':'true' , # 跳过设备初始化
            'settings[waitForIdleTimeout]':0  # 等待Idle为0
        }

        #与server建立连接，初始化一个driver，创建session
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 销毁session
        self.driver.quit()

    def test_daka(self):
        """
        1. 打开企业微信APP
        2. 点击【工作台】
        3. 在【工作台】滚动查找到【打卡】，然后点击
        4. 切换到【外出打卡】
        5. 选中打开范围，点击
        6. 断言
        :return:
        """

        #点击【工作台】
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()

        #在【工作台】滚动查找到【打卡】，然后点击
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                    'scrollIntoView(new UiSelector().text("打卡").instance(0))').click()
        #切换到【外出打卡】
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/gw8').click()

        # 选中打开范围，点击
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/ao_').click()

        #断言
        assert_content = self.driver.find_element(MobileBy.XPATH,'//*[contains(@text,"打卡成功")]').text

        assert "打卡成功" in assert_content