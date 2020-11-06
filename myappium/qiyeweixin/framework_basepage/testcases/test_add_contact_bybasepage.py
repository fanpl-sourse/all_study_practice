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
        self.app = App()
        self.app_start = self.app.start()

    def teardown_class(self):
        self.app.stop()

    def teardown(self):
        self.app.back()

    @pytest.mark.parametrize(('name,gender,mobilenum'),addcontacts)
    def test_add_contact(self,name,gender,mobilenum):
        """
        测试企业微信-通讯录-新增联系人
        """
        self.app.goto_main().goto_contact().goto_manual_add_contact_page().goto_add_contact_page().\
            send_name(name).\
            click_gender(gender).\
            send_mobilenum(mobilenum).\
            click_save().assert_add_success()


    @pytest.mark.parametrize(('name'),delcontacts)
    def test_del_contact(self,name):
        """
        测试企业微信-通讯录-删除联系人
        :param name:
        :return:
        """
        #启动APP-进入联系人列表页-进入检索框页面
        searchpage = self.app.goto_main().goto_contact().goto_search_page()
        #获取搜索前的页面数据列表
        before_list = searchpage.send_search_key(name)

        #-进入个人信息页面-进入个人信息设置页面-进入编辑页面，进行删除动作，此时回到检索框列表页
        after_delete_returnto_searchPage = searchpage.goto_personal_info_page(before_list).\
                                                      goto_personal_info_setting_page().\
                                                      goto_edit_member_page().delete_member()
        #删除后再次检索，获取检索后的页面数据列表
        after_list = after_delete_returnto_searchPage.send_search_key(name)
        #断言
        after_delete_returnto_searchPage.assert_search_result(len(before_list),len(after_list))






