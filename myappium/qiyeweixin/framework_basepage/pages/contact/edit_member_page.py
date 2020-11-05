# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 08:34
# @Author  : 饭盆里
# @File    : personal_info_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage


class EditMemberPage(BasePage):
    """
    编辑成员信息页面
    """
    deletemember_text = "删除成员"
    click_confirm_element = (MobileBy.ID, 'com.tencent.wework:id/bci')

    def delete_member(self):
        """
        删除成员
        :return:
        """
        # 滚动查找到【删除成员】按钮，点击
        self.find_by_scroll(self.deletemember_text)
        # 确认删除
        self.find_and_click(self.click_confirm_element)

        from myappium.qiyeweixin.framework_basepage.pages.contact.search_page import SearchPage
        return SearchPage(self.driver)

