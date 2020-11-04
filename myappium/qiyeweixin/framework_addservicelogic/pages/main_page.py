# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:17
# @Author  : 饭盆里
# @File    : main_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy

from myappium.qiyeweixin.framework_addservicelogic.pages.contact.contact_list_page import ContactListPage

class MainPage:
    """
    企业微信主页面
    """
    def __init__(self,driver):
        self.driver = driver

    def goto_contact(self):
        """
        进入通讯录列表页
        :return:
        """
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return ContactListPage(self.driver)

    def goto_workplatform(self):
        """
        进入工作台
        :return:
        """
