# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 08:31
# @Author  : 饭盆里
# @File    : workspace_list_page.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework.pages.workspace.punch_page import PunchPage

class WorkspaceListPage():
    """
    工作台列表页页面
    """
    def goto_punch_page(self):
        """
        进入打卡页面
        :return:
        """
        return PunchPage()