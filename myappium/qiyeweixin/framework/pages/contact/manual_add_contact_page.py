# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:23
# @Author  : 饭盆里
# @File    : manual_add_contact_page.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework.pages.contact.add_contact_page import AddContactPage


class ManualAddContactPage:
    """
    添加成员菜单页
    """

    def goto_add_contact_page(self):
        """
        进入添加成员页
        :return:
        """
        return AddContactPage()