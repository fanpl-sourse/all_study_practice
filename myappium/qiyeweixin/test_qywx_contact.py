# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 20:01
# @Author  : 饭盆里
# @File    : test_qywx_contact.py
# @Software: PyCharm
# @desc    : 企业微信联系人相关
""""
优化项
1. 性别判断
2. 断言
3. 显示等待
4. 滚动查找 添加用户
4. 参数化
   参数化运行的时候希望不重启APP，需要在案例运行结束后进入通讯录页面
"""
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

with open('./data/addcontact.yaml') as f:
    addcontacts = yaml.safe_load(f)

with open('./data/delcontact.yaml') as f:
    delcontacts = yaml.safe_load(f)

class TestQywxContact:
    def setup_class(self):
        desire_caps = {
            "platformName": "android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "deviceName": "emulator-5554",
            "noReset": "true",
            'skipServerInstallation': 'true',  # 跳过 uiautomator2 server的安装
            'skipDeviceInitialization': 'true',  # 跳过设备初始化
            'settings[waitForIdleTimeout]': 0 , # 等待Idle为0
            'dontStopAppOnReset':'true'        #不关闭，重启APP
        }

        # 与server建立连接，初始化一个driver，创建session
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(5)

    def teardown_class(self):

        # 销毁session
        self.driver.quit()

    #参数化
    # @pytest.mark.parametrize('name,gender,mobile',[
    #     ("fanfan10","男","18700000010"),
    #     ("fanfan09", "女", "18700000009"),
    # ])
    @pytest.mark.parametrize('name,gender,mobile',addcontacts)
    def test_add_contact(self,name,gender,mobile):
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
        # name = "fanfan05"
        # gender = "男"
        # mobile = "18700000005"

        #点击通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()

        #点击添加成员-->>滚动查找到这个元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        #点击手动输入添加
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/hgx').click()

        #输入【用户名】
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys(name)

        #性别
        self.driver.find_element(MobileBy.XPATH,'//*[@text="性别"]/..//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 f'//*[@resource-id="com.tencent.wework:id/dyx" and @text="{gender}"]').click()

        #输入手机号
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/f1e').send_keys(mobile)
        #保存
        self.driver.find_element(MobileBy.XPATH,'//*[@text="保存"]').click()

        #断言 toast
        toast_message = self.driver.find_element(MobileBy.XPATH,'//*[@class="android.widget.Toast"]').text

        assert '添加成功' in toast_message
        #返回到列表页
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/h9e').click()


    @pytest.mark.parametrize('name',delcontacts)
    def test_del_contact(self,name):
        """
        1. 打开应用
        2. 点击通讯录
        3. 找到要删除的联系人
        4. 进入联系人页面
        5. 点击右上角的三个点进入个人信息页面，点击编辑成员
        6. 删除联系人
        7. 确认删除
        8. 验证删除成功
        :return:
        """

        # name = 'fanfan11'

        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        # 找到要删除的联系人
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h9z').click()
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/fxc').send_keys(name)
        sleep(2)
        search_element_list = self.driver.find_elements(MobileBy.XPATH,f'//*[@text="{name}"]')
        if len(search_element_list) <= 1:
            print('没有找到要删除的数据')
            return
        search_element_list[-1].click()

        print(len(search_element_list))

        # 点击右上角的三个点进入个人信息页面，点击编辑成员
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/h9p').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="编辑成员"]').click()

        # 滚动查找到【删除成员】按钮，点击
        text = '删除成员'
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
        #                                                 f'.scrollIntoView(new UiSelector().text("{text}").instance(0));').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                 f'.scrollIntoView(new UiSelector().text("{text}").instance(0))').click()

        # 确认删除
        self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/bci').click()

        # 验证删除成功
        sleep(2)
        search_element_list_after = self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{name}"]')
        sleep(2)
        print(len(search_element_list_after))
        assert len(search_element_list) - len(search_element_list_after) == 1


