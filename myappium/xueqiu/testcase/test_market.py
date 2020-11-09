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
        """
        通过行情，检索股票，并加关注
        :return:
        """
        self.app.goto_mainpage().goto_market().goto_search_stock().search_stock('阿里巴巴','09988').\
            add_mychoice('09988').assert_add_mychoice_success('09988')