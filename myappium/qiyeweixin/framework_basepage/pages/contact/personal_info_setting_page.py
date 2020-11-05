# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 08:34
# @Author  : 饭盆里
# @File    : personal_info_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.contact.edit_member_page import EditMemberPage


class PersonalInfoSettingPage(BasePage):
    """
    个人信息页面-设置
    """

    editmember_element = (MobileBy.XPATH, '//*[@text="编辑成员"]')

    def goto_edit_member_page(self):
        """
        点击编辑成员按钮，进入编辑用户页面
        :return:
        """
        self.find_and_click(self.editmember_element)
        return EditMemberPage(self.driver)

