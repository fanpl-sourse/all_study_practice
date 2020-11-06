# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 08:31
# @Author  : 饭盆里
# @File    : workspace_list_page.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.workspace.punch_page import PunchPage

class WorkspaceListPage(BasePage):
    """
    工作台列表页页面
    """

    punch_text = "打卡"

    def goto_punch_page(self):
        """
        进入打卡页面
        :return:
        """
        # 在【工作台】滚动查找到【打卡】，然后点击
        self.find_by_scroll(self.punch_text)

        return PunchPage(self.driver)