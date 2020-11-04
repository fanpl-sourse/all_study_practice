# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:33
# @Author  : 饭盆里
# @File    : test_add_contact_bybasepage.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework_addservicelogic.basepage.app import App


class TestAddContact:
    def setup(self):
        self.APP = App()

    def test_contact(self):
        self.APP.start().goto_contact().goto_manual_add_contact_page().goto_add_contact_page().\
            send_name('fanpl3').\
            click_gender('女').\
            send_mobilenum('18388888881').\
            click_save().assert_add_success()