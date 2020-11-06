# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 08:42
# @Author  : 饭盆里
# @File    : test_workspace_punch_outside.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework_basepage.basepage.app import App


class TestWorkspacePunchOutside:
    """
    测试工作台-打卡-外出打卡
    """
    def setup(self):
        """
        :return:
        """
        self.app = App()
        self.app_start = self.app.start()

    def teardown(self):
        self.app.stop()


    def test_outside_punch(self):
        """
        测试外出打卡
        :return:
        """
        self.app.goto_main().goto_workplatform().goto_punch_page().\
            switchto_outside_punch().outside_punch().assert_punch_success()