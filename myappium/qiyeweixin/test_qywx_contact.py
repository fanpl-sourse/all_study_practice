# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 20:01
# @Author  : 饭盆里
# @File    : test_qywx_contact.py
# @Software: PyCharm
# @desc    : 企业微信联系人相关
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestQywxContact:
    def setup(self):
        desire_caps = {
            "platformName": "android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "deviceName": "emulator-5554",
            "noReset": "true",
            'skipServerInstallation': 'true',  # 跳过 uiautomator2 server的安装
            'skipDeviceInitialization': 'true',  # 跳过设备初始化
            'settings[waitForIdleTimeout]': 0  # 等待Idle为0
        }

        # 与server建立连接，初始化一个driver，创建session
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 销毁session
        self.driver.quit()

    def test_add_contact(self):
        """
        1. 打开应用
        2. 点击通讯录
        3. 点击添加成员
        4. 手动输入添加
        5. 输入【用户名】、性别、手机号
        6. 点击保存
        7. 验证添加成功
        :return:
        """
        #点击通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        #点击添加成员
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]').click()
        #点击手动输入添加
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hgx').click()
        #输入【用户名】、性别、手机号
        self.driver.find_element(MobileBy.XPATH,'//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys('fanfan02')

        self.driver.find_element(MobileBy.XPATH,'//*[@text="性别"]/..//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@resource-id="com.tencent.wework:id/dyx" and @text="女"]').click()

        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/f1e').send_keys('18700000001')
        #保存
        self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()
