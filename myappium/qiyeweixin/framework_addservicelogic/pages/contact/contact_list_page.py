# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:19
# @Author  : 饭盆里
# @File    : contact_list_page.py
# @Software: PyCharm
# @desc    :
from appium import webdriver
from myappium.qiyeweixin.framework_addservicelogic.pages.contact.manual_add_contact_page import ManualAddContactPage


class ContactListPage:
    """
    通讯录列表页
    """

    def __init__(self,driver:webdriver):
        self.driver = driver

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
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()

        return ManualAddContactPage(self.driver)
