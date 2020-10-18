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
from mypytest.util.readyaml import Util

datas = Util().readyaml('../data/cacl_md_data.yaml')
for key in datas:
    if key == 'mut':
        mymut = datas['mut']
        mymutkeys = mymut.keys()
        mymutvalues = mymut.values()
    elif key == 'div':
        mydiv = datas['div']
        mydivkeys = mydiv.keys()
        mydivvalues = mydiv.values()


class TestCacl():
    def setup(self):
        print('setup')

    @classmethod
    def setup_class(self):
        self.cacl = Cacl()
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
    # @pytest.mark.parametrize(('a,b,c'),yaml.safe_load(open('../data/cacl_data.yaml')))
    @pytest.mark.parametrize(('a,b,c'),Util().readyaml('../data/cacl_data.yaml'))
    def test_mysub(self,a,b,c):
        assert c == self.cacl.mysub(a,b)


    @pytest.mark.mymut
    @pytest.mark.parametrize(('a,b,c'),mymutvalues,ids=mymutkeys)
    def test_mymut2(self,a,b,c):
        assert c == self.cacl.mymut(a,b)


    @pytest.mark.parametrize(('a,b,c'),mydivvalues,ids=mydivkeys)
    def test_mydiv(self,a,b,c):
        try:
            assert c == self.cacl.mydiv(a,b)
        except ZeroDivisionError as es:
            print('除数为0')