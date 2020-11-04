# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:23
# @Author  : 饭盆里
# @File    : manual_add_contact_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy

from myappium.qiyeweixin.framework_addservicelogic.pages.contact.add_contact_page import AddContactPage


class ManualAddContactPage:
    """
    添加成员菜单页
    """

    def __init__(self,driver):
        self.driver = driver

    def goto_add_contact_page(self):
        """
        进入添加成员页
        :return:
        """
        # 点击手动输入添加
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hgx').click()
        return AddContactPage(self.driver)

    def assert_add_success(self):
        """
        断言新建联系人成功
        :return:
        """
        # 断言 toast
        toast_message = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        assert '添加成功' in toast_message