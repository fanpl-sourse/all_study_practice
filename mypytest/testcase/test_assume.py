# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 17:36
# @Author  : 饭盆里
# @File    : test_assume.py
# @Software: PyCharm
# @desc    : 多条断言
import pytest

class TestAssert():
    def testcase(self):
        print('testcase')
        pytest.assume(1==4)
        pytest.assume(2==2)
        pytest.assume(3==0)
