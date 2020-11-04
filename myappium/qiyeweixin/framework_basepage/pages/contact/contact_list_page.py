# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:19
# @Author  : 饭盆里
# @File    : contact_list_page.py
# @Software: PyCharm
# @desc    :
from appium import webdriver

from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.contact.manual_add_contact_page import ManualAddContactPage


class ContactListPage(BasePage):
    """
    通讯录列表页
    """

    text = "添加成员"

    def search_contact(self):
        """
        搜索联系人
        :return:
        """

    def goto_manual_add_contact_page(self):
        """
        进入手动添加联系人页面
        :return:
        """
        # 点击添加成员-->>滚动查找到这个元素

        self.find_by_scroll(self.text)
        return ManualAddContactPage(self.driver)
