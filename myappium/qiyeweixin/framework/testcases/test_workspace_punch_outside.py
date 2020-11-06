# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 08:42
# @Author  : 饭盆里
# @File    : test_workspace_punch_outside.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework.basepage.app import App


class TestWorkspacePunchOutside:
    """
    测试工作台-打卡-外出打卡
    """
    def setup(self):
        """

        :return:
        """
        self.App = App()


    def test_outside_punch(self):
        """
        测试外出打卡
        :return:
        """
        self.App.start().goto_workplatform().goto_punch_page().switchto_outside_punch().outside_punch()