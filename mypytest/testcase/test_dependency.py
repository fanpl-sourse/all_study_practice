# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 17:42
# @Author  : 饭盆里
# @File    : test_dependency.py
# @Software: PyCharm
# @desc    : 用例之间的依赖关系
import pytest


class TestDependency():
    @pytest.mark.dependency(name='test_a')
    def test_a(self):
        print('test_a')
        assert True

    @pytest.mark.dependency(name='test_b')
    def test_b(self):
        print('test_b')
        assert False

    @pytest.mark.dependency(depends=['test_a'])
    def test_c(self):
        print('test_c')

    @pytest.mark.dependency(depends=['test_b'])
    def test_d(self):
        print('test_d')

    @pytest.mark.dependency(depends=['test_a','test_b'])
    def test_e(self):
        print('test_e')