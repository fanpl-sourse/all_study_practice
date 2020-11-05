# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:19
# @Author  : 饭盆里
# @File    : contact_list_page.py
# @Software: PyCharm
# @desc    :
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.contact.manual_add_contact_page import ManualAddContactPage
from myappium.qiyeweixin.framework_basepage.pages.contact.personal_info_page import PersonalInfoPage
from myappium.qiyeweixin.framework_basepage.pages.contact.search_page import SearchPage


class ContactListPage(BasePage):
    """
    通讯录列表页
    """

    text = "添加成员"
    click_search_element = (MobileBy.ID, 'com.tencent.wework:id/h9z')

    def goto_search_page(self):
        """
        点击搜索图标进入搜索框页面
        :return:
        """
        #点击搜索框
        self.find_and_click(self.click_search_element)
        return SearchPage(self.driver)


    def goto_manual_add_contact_page(self):
        """
        进入手动添加联系人页面
        :return:
        """
        # 点击添加成员-->>滚动查找到这个元素

        self.find_by_scroll(self.text)
        return ManualAddContactPage(self.driver)
