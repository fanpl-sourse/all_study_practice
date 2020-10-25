# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 15:29
# @Author  : 饭盆里
# @File    : test_homepo.py
# @Software: PyCharm
# @desc    :
import pytest

from myUIautotest.wework.homePo.home_po import HomePo


class TestHomepo():
    def setup(self):
        self.homepo = HomePo()

    def teardown(self):
        pass

    def test_homepo_gotologin(self):
        """
        测试首页的进入登录
        :return:
        """
        self.homepo.goto_login()

    def test_homepo_gotoregister(self):
        """
        测试首页的进入注册
        :return:
        """
        self.homepo.goto_register()

    def test_loginpo_gotoregister(self):
        """
        测试登录页面的进入注册函数
        :return:
        """
        self.homepo.goto_login().goto_register()

    @pytest.mark.parametrize(('corp_name,manager_name,register_tel'),[
        ("组织名称","管理人名称","18200000000")
    ])
    def test_registorpo_register(self,corp_name,manager_name,register_tel):
        """
        测试注册页面的注册函数
        :return:
        """
        self.homepo.goto_register().registor(corp_name,manager_name,register_tel)