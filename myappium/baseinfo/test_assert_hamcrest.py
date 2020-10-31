# -*- coding: utf-8 -*-
# @Time    : 2020/10/31 10:50
# @Author  : 饭盆里
# @File    : test_assert_hamcrest.py
# @Software: PyCharm
# @desc    : 断言
from hamcrest import *


class TestAssertHamcrest:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_assert(self):
        a=10
        b=20
        assert a==b

    def test_hamcrest_equalto(self):
        a = 10
        b = 10
        assert_that(a,equal_to(b))


    def test_hamcrest_closeto(self):
        a=10
        b=5
        assert_that(a,close_to(b,5))

    def test_hamcrest_ends_with(self):
        a='hi'
        b='jghjdkhi'
        assert_that(b,ends_with(a))

    def test_hamcrest_contains_string(self):
        a = 'hi'
        b = 'hi1'
        assert_that(b,contains_string(a))

    def test_hamcrest_greater_than(self):
        a=10
        b=20
        assert_that(b,greater_than(a))