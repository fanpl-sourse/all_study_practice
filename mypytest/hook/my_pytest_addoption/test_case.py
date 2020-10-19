# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 09:47
# @Author  : 饭盆里
# @File    : test_case.py
# @Software: PyCharm
# @desc    :


class TestCase():

    def test_env(self,read_envdata):
        myenv,mydatas = read_envdata
        print(myenv)
        print(mydatas)
