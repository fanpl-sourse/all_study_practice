# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 16:59
# @Author  : 饭盆里
# @File    : test_wasper.py
# @Software: PyCharm
# @desc    :
"""
装饰器原理
"""

#传入一个函数名
def wasper(fun):
    def he(*args,**kwargs):
        print('hello')
        fun()
        print('bye')
    #返回一个函数名
    return he

@wasper
def fun():
    print('fun')

def fun1():
    print('fun1')

def test():
    #太繁琐了
    wasper(fun1)()
    fun()