# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:26
# @Author  : 饭盆里
# @File    : add_contact_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy


class AddContactPage:
    """
    添加成员的操作页面
    """

    def __init__(self,driver):
        self.driver = driver

    def send_name(self,name):
        """
        输入姓名
        :return:
        """
        # 输入【用户名】
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]').send_keys(name)

        return self

    def click_gender(self,gender):
        """
        点击选择性别
        :return:
        """
        # 性别
        self.driver.find_element(MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH,
                                 f'//*[@resource-id="com.tencent.wework:id/dyx" and @text="{gender}"]').click()

        return self

    def send_mobilenum(self,mobile):
        """
        输入手机号
        :return:
        """
        # 输入手机号
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/f1e').send_keys(mobile)
        return self

    def click_save(self):
        """
        点击保存
        :return:
        """
        from myappium.qiyeweixin.framework_addservicelogic.pages.contact.manual_add_contact_page import \
            ManualAddContactPage
        # 保存
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        return ManualAddContactPage(self.driver)

