# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:33
# @Author  : 饭盆里
# @File    : test_add_contact_bybasepage.py
# @Software: PyCharm
# @desc    :
import pytest
import yaml

from myappium.qiyeweixin.framework_basepage.basepage.app import App

with open('../../data/addcontact.yaml') as f:
    addcontacts = yaml.safe_load(f)

with open('../../data/delcontact.yaml') as f:
    delcontacts = yaml.safe_load(f)


class TestAddContact:
    def setup_class(self):
        self.APP = App()

    def teardown_class(self):
        self.APP.stop()

    @pytest.mark.parametrize(('name,gender,mobilenum'),addcontacts)
    def test_contact(self,name,gender,mobilenum):
        self.APP.start().goto_contact().goto_manual_add_contact_page().goto_add_contact_page().\
            send_name(name).\
            click_gender(gender).\
            send_mobilenum(mobilenum).\
            click_save().assert_add_success()

        self.APP.back()