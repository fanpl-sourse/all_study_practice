# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 11:10
# @Author  : 饭盆里
# @File    : test_fixture.py
# @Software: PyCharm
# @desc    : fixture 装饰方法

import pytest

# @pytest.fixture(scope="class")
# def login():
#     print('这是登录')
#     yield
#     print('调用login并执行完用例后执行')

class TestParacases1():

    @pytest.mark.parametrize(('a,b,c'),[
        (1,2,3),
        (4.3,5.3,9.6),
        (-2,-4,-6)
    ],ids=['int','float','minus'])
    def test_myadd1(self,a,b,c):
        print(f'{a} + {b} = {c}')

    def test_case11(self,login):
        print('test_case11')

    def test_case12(self):
        print('test_case12')

    def test_case13(self,login):
        print('test_case13')

class TestParacases2():

    @pytest.mark.parametrize(('a,b,c'),[
        (1,2,3),
        (4.3,5.3,9.6),
        (-2,-4,-6)
    ],ids=['int','float','minus'])
    def test_myadd2(self,a,b,c):
        print(f'{a} + {b} = {c}')

    def test_case21(self):
        print('test_case21')

    @pytest.mark.parametrize('fixture_para',['data1','data2'],indirect=True)
    @pytest.mark.parametrize(('a,b'),[
        (1,2),
        (3,4)
    ])
    def test_case22(self,fixture_para,a,b):
        print(f'test_case22，{fixture_para}')
        print(f'参数：{a},{b}')

    def test_case23(self,login):
        print('test_case23')
