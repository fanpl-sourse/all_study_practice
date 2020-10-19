# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 11:19
# @Author  : 饭盆里
# @File    : testcase.py
# @Software: PyCharm
# @desc    : 注意区分
import pytest
import yaml

with open('data/data.yaml') as f:
    datas = yaml.safe_load(f)
    mydatas = datas.values()
    myids = datas.keys()

class TestCase():

    @pytest.mark.parametrize(('a,b,c'),mydatas,ids=myids)
    def test_case(self,a,b,c):
        print(f'测试场景：{a},{b},{c}')


    def test_case1(self,param):
        print(f'{param}')
