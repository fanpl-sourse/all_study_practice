# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:17
# @Author  : 饭盆里
# @File    : main_page.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework.pages.contact.contact_list_page import ContactListPage
from myappium.qiyeweixin.framework.pages.workspace.workspace_list_page import WorkspaceListPage


class MainPage:
    """
    企业微信主页面
    """
    def goto_contact(self):
        """
        进入通讯录列表页
        :return:
        """
        return ContactListPage()

    def goto_workplatform(self):
        """
        进入工作台
        :return:
        """
        return WorkspaceListPage()
