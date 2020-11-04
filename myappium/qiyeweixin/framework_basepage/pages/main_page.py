# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:17
# @Author  : 饭盆里
# @File    : main_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy

from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.contact.contact_list_page import ContactListPage

class MainPage(BasePage):
    """
    企业微信主页面
    """

    click_contact_element = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_contact(self):
        """
        进入通讯录列表页
        :return:
        """
        # 点击通讯录

        self.find_and_click(self.click_contact_element)
        return ContactListPage(self.driver)

    def goto_workplatform(self):
        """
        进入工作台
        :return:
        """
