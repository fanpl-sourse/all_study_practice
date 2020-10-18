# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 17:57
# @Author  : 饭盆里
# @File    : test_thread.py
# @Software: PyCharm
# @desc    : 并发  运行命令：pytest -vs test_thread.py -n 3
from time import sleep

class TestThread():
    def testcase1(self):
        print('testcase1')
        sleep(2)

    def testcase2(self):
        print('testcase2')
        sleep(2)

    def testcase3(self):
        print('testcase3')
        sleep(2)

    def testcase4(self):
        print('testcase4')
        sleep(2)

    def testcase5(self):
        print('testcase5')
        sleep(2)

    def testcase6(self):
        print('testcase6')
        sleep(2)