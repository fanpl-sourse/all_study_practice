# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 20:12
# @Author  : 饭盆里
# @File    : test_case.py
# @Software: PyCharm
# @desc    :
import pytest


class Testcase():
    def testcase(self):
        print('testcase')

    @pytest.mark.parametrize(('a,b'),[(1,2),(3.4,4.5)],ids=['整数','小数'])
    def testcase1(self,a,b):
        print('testcase1')
        print(f'{a},{b}')

    def testcase2(self):
        print('testcase2')

    def testcase3(self):
        print('testcase3')