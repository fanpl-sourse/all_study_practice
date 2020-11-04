# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:26
# @Author  : 饭盆里
# @File    : add_contact_page.py
# @Software: PyCharm
# @desc    :
class AddContactPage:
    """
    添加成员的操作页面
    """

    def send_name(self):
        """
        输入姓名
        :return:
        """
        return self

    def click_gender(self):
        """
        点击选择性别
        :return:
        """
        return self

    def send_mobilenum(self):
        """
        输入手机号
        :return:
        """
        return self

    def click_save(self):
        """
        点击保存
        :return:
        """
        from myappium.qiyeweixin.framework.pages.contact.manual_add_contact_page import ManualAddContactPage
        return ManualAddContactPage()