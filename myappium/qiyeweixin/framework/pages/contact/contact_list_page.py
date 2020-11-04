# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:19
# @Author  : 饭盆里
# @File    : contact_list_page.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework.pages.contact.manual_add_contact_page import ManualAddContactPage


class ContactListPage:
    """
    通讯录列表页
    """
    def search_contact(self):
        """
        搜索联系人
        :return:
        """

    def goto_manual_add_contact_page(self):
        """
        进入手动添加联系人页面
        :return:
        """

        return ManualAddContactPage()
