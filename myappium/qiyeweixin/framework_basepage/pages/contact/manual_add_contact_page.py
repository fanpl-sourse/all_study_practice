# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:23
# @Author  : 饭盆里
# @File    : manual_add_contact_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy

from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.contact.add_contact_page import AddContactPage


class ManualAddContactPage(BasePage):
    """
    添加成员菜单页
    """

    manual_add_click = (MobileBy.ID, 'com.tencent.wework:id/hgx')
    toast_element = (MobileBy.XPATH, '//*[@class="android.widget.Toast"]')

    def goto_add_contact_page(self):
        """
        进入添加成员页
        :return:
        """
        # 点击手动输入添加

        self.find_and_click(self.manual_add_click)
        return AddContactPage(self.driver)

    def assert_add_success(self):
        """
        断言新建联系人成功
        :return:
        """
        # 断言 toast

        # toast_message = self.find(self.toast_element)
        toast_message = self.webdriver_wait(self.toast_element,20)
        assert '添加成功' in toast_message.text