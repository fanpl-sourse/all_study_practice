# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 10:39
# @Author  : 饭盆里
# @File    : test_market.py
# @Software: PyCharm
# @desc    :
from myappium.xueqiu.page.app import App


class TestMarket:
    def setup(self):
        self.app = App().start()

    def test_search_stock(self):
        self.app.goto_mainpage().goto_market().goto_search_stock().search_stock().\
            add_mychoice().assert_add_mychoice_success()