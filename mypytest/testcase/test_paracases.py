# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 10:50
# @Author  : 饭盆里
# @File    : test_paracases.py
# @Software: PyCharm
# @desc    : 参数化用例
import pytest
import yaml


class TestParacases():

    # @pytest.mark.flaky(reruns=5)
    @pytest.mark.parametrize(('a,b,c'),[
        (1,2,3.1),
        (4.3,5.3,9.6),
        (-2,-4,-6)
    ],ids=['int','float','minus'])
    def test_myadd(self,a,b,c):
        assert c == a+b

    @pytest.mark.parametrize(('a,b,c'),yaml.safe_load(open('../data/cacl_data.yaml')))
    def test_readyaml(self,a,b,c):
        print(f'a = {a},b = {b},c = {c}')

