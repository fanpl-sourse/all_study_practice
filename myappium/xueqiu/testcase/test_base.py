# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 15:04
# @Author  : 饭盆里
# @File    : test_base.py
# @Software: PyCharm
# @desc    :
from myappium.xueqiu.page.app import App


class TestBase:
    """
    测试用例的基础封装，比如断言的通用封装（断言前后进行截图），初始化APP的通用封装
    """
    app = None
    def setup(self):
        self.app = App()
        self.app.start()