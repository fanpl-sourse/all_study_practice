# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 10:30
# @Author  : 饭盆里
# @File    : test_order.py
# @Software: PyCharm
# @desc    : 练习pytest运行顺序，需要提前安装order
import pytest


class TestOrder():
    @pytest.mark.run(order=-1)
    def test_case1(self):
        print('test_case1')

    @pytest.mark.last
    def test_case2(self):
        print('test_case2')

    def test_case3(self):
        print('test_case3')

    @pytest.mark.run(order=1)
    def test_case4(self,fixture_sendpara):
        print('test_case4')

    def test_aaa(self):
        print('这个执行顺序是？？')