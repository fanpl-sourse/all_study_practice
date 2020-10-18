# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 15:57
# @Author  : 饭盆里
# @File    : test_cacl.py
# @Software: PyCharm
# @desc    : 测试脚本
import os
import sys

import pytest
import yaml
from mypytest.cacl.cacl import Cacl

class TestCacl():
    def setup(self):
        self.cacl = Cacl()
        print('setup')

    @classmethod
    def setup_class(cls):
        cls.cacl = Cacl()
        print('setupclass')
    @classmethod
    def teardown_class(cls):
        print('teardownclass')

    @pytest.mark.myadd
    @pytest.mark.parametrize(('a,b,c'),[
        (1,2,3),
        (-1,-2,-3),
        (-1,8,7),
        (-1.3,2.5,1.2),
        (2,3,5)
    ])
    def test_myadd(self,a,b,c):
        assert c == self.cacl.myadd(a,b)

    @pytest.mark.mysub
    @pytest.mark.parametrize(('a,b,c'),yaml.safe_load(open('../data/cacl_data.yaml')))
    def test_mysub(self,a,b,c):
        assert c == self.cacl.mysub(a,b)
