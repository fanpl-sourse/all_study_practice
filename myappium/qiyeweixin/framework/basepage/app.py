# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:14
# @Author  : 饭盆里
# @File    : app.py
# @Software: PyCharm
# @desc    :
from myappium.qiyeweixin.framework.pages.main_page import MainPage


class App:
    """
    APP相关动作
    """
    def start(self):
        """
        启动APP
        :return:
        """
        return MainPage()

    def restart(self):
        """
        重启APP
        :return:
        """
        return MainPage()

    def stop(self):
        """
        停止APP
        :return:
        """
        pass