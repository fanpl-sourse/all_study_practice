# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:33
# @Author  : 饭盆里
# @File    : test_search_stock.py
# @Software: PyCharm
# @desc    :
import pytest
import yaml

from myappium.xueqiu.page.app import App


class TestSearchStock:
    def setup(self):
        self.app = App()
        self.app.start()

    # def teardown(self):
    #     self.app

    def test_search_stock(self):
        """
        进入雪球APP-雪球APP首页-检索页-检索结果页-检索结果详情页
        :return:
        """
        self.app.goto_mainpage().goto_search_page().goto_search_result_page('阿里巴巴').goto_search_result_detail_page()


    def test_blackmenu(self):
        """
        对意料之外的弹框的处理，比如：APP好评，广告等
        :return:
        """
        self.app.goto_mainpage().goto_black_then_goto_search()
