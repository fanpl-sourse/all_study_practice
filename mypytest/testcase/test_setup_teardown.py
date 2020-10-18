# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 09:56
# @Author  : 饭盆里
# @File    : test_setup_teardown.py
# @Software: PyCharm
# @desc    : 练习框架 setup teardown

def setup_module():
    print('setup_module 在模块前调用')

def teardown_module():
    print('teardown_module 在模块后调用')

class TestClass1():
    def setup(self):
        print('setup 在类1方法前调用')

    def teardown(self):
        print('teardown 在类1方法后调用')

    def setup_class(self):
        print('setup_class 在类1前调用')

    def teardown_class(self):
        print('teardown_class 在类1后调用')
        print('*'*50)


    def test_case1(self):
        print('这是要测试的方法1')

    def test_case2(self):
        print('这是要测试的方法2')

class TestClass2():
    def setup(self):
        print('setup 在类2方法前调用')

    def teardown(self):
        print('teardown 在类2方法后调用')

    def setup_class(self):
        print('setup_class 在类2前调用')

    def teardown_class(self):
        print('teardown_class 在类2后调用')

    def test_case3(self):
        print('这是要测试的方法3')

    def test_case4(self):
        print('这是要测试的方法4')