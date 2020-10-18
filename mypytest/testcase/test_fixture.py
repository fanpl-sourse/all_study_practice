# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 11:10
# @Author  : 饭盆里
# @File    : test_fixture.py
# @Software: PyCharm
# @desc    : fixture 装饰方法

import pytest

@pytest.fixture()
def login():
    print('这是登录')

class TestParacases():

    @pytest.mark.parametrize(('a,b,c'),[
        (1,2,3),
        (4.3,5.3,9.6),
        (-2,-4,-6)
    ],ids=['int','float','minus'])
    def test_myadd(self,a,b,c):
        print(f'{a} + {b} = {c}')

    def test_case(self,login):
        print('test_case')
