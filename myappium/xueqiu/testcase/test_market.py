# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 10:39
# @Author  : 饭盆里
# @File    : test_market.py
# @Software: PyCharm
# @desc    :
import os

import pytest

from myappium.xueqiu.page.app import App
from myappium.xueqiu.tools.readyaml import Tools


class TestMarket:
    def setup(self):
        self.app = App().start()

    # @pytest.mark.parametrize(('stock_name,stock_num'),[
    #     ('阿里巴巴','09988'),
    #     ('京东','JD')
    # ])
    @pytest.mark.parametrize(('stock_name,stock_num'),Tools().read_yaml('../data/market_data.yaml'))
    def test_search_stock(self,stock_name,stock_num):
        """
        通过行情，检索股票，并加关注
        :return:
        """
        self.app.goto_mainpage().goto_market().goto_search_stock().search_stock(stock_name,stock_num).\
            add_mychoice(stock_num).assert_add_mychoice_success(stock_num)
