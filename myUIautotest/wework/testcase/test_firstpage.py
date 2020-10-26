# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 17:10
# @Author  : 饭盆里
# @File    : test_firstpage.py
# @Software: PyCharm
# @desc    :
import pytest

from myUIautotest.wework.addressPo.firstpage_po import FirstPagePo


class TestFirstPage():
    def setup(self):
        self.firstpagepo = FirstPagePo()

    def teardown(self):
        pass

    def test_firstpage_goto_address(self):
        '''
        从首页进入通讯录
        :return:
        '''
        self.firstpagepo.goto_address()

    @pytest.mark.parametrize(('username,mobile'),[
        ('fanfanfan001','18700000111')
    ])
    def test_firstpage_goto_address_addmember(self,username,mobile):
        """
        从首页进入通讯录后，进行新增成员操作
        :return:
        """
        self.firstpagepo.goto_address().goto_add_address().add_address(username,mobile)