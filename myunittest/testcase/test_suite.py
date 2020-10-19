# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 11:37
# @Author  : 饭盆里
# @File    : test_suite.py
# @Software: PyCharm
# @desc    :
import unittest

from myunittest.testcase.test_unittest import TestMethods
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMethods('test_split'))
    suite.addTest(TestMethods('test_isupper'))
    runner = unittest.TextTestRunner()
    runner.run(suite)