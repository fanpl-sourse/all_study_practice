# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:33
# @Author  : 饭盆里
# @File    : test_add_contact.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework.basepage.app import App


class Test:
    def setup(self):
        self.driver = App()

    def test_contact(self):
        self.driver.start().goto_contact().goto_manual_add_contact_page().goto_add_contact_page().click_gender()