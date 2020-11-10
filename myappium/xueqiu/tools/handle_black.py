# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 17:08
# @Author  : 饭盆里
# @File    : handle_black.py
# @Software: PyCharm
# @desc    : 处理黑名单

#装饰器函数--处理黑名单
# 入参是一个函数名，出参也是一个函数名
from selenium.webdriver.common.by import By


def handle_black(func):
    _blacklist = {(By.ID, 'com.xueqiu.android:id/iv_close'),
                  (By.ID,'com.xueqiu.android:id/ib_close')
                  }
    #支持传任何参数
    def warper(*args,**kwargs):
        #局部引用，方式循环调用  instance 变量是获取传入函数的第一个变量，self
        from myappium.xueqiu.page.basepage import BasePage
        instance:BasePage = args[0]
        try:
                #模拟被调用函数的动作，比如 查找元素
                element = func(*args,**kwargs)
                instance._black_error_num = 0
                instance.driver.implicitly_wait(10)
                return element
        except Exception as e:
            instance.driver.implicitly_wait(1)
            if instance._black_error_num >instance._black_error_max_num:
                instance._black_error_num = 0
                return e
            instance._black_error_num += 1
            for black in _blacklist:
                elements = instance.driver.find_elements(*black)
                if len(elements) >0:
                    elements[0].click()
                    #递归调用，关闭弹框后，继续查找要找的元素
                    return warper(*args,**kwargs)
            raise ValueError('元素不在黑名单中')

    return warper
