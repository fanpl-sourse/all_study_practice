# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 08:34
# @Author  : 饭盆里
# @File    : personal_info_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.contact.personal_info_setting_page import PersonalInfoSettingPage

class PersonalInfoPage(BasePage):
    """
    个人信息页面
    """

    threepoint_element = (MobileBy.ID, 'com.tencent.wework:id/h9p')

    def goto_personal_info_setting_page(self):
        """
        点击右上角的三个点,进入用户信息设置页面
        :return:
        """
        self.find_and_click(self.threepoint_element)
        return PersonalInfoSettingPage(self.driver)

