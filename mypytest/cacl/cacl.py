# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 13:55
# @Author  : 饭盆里
# @File    : cacl.py
# @Software: PyCharm
# @desc    : 计算器的加减乘除

class Cacl:

    def myadd(self,a,b):
        '''
        加法
        :param a:
        :param b:
        :return:
        '''
        return a+b

    def mysub(self,a,b):
        """
        减法
        :param a:
        :param b:
        :return:
        """
        return a-b

    def mymut(self,a,b):
        """
        乘法
        :param a:
        :param b:
        :return:
        """
        return a*b

    def mydiv(self,a,b):
        """
        除法
        :param a:
        :param b:
        :return:
        """
        return a/b

if __name__ == '__main__':
    cacl = Cacl()
    print(cacl.myadd(1,2))