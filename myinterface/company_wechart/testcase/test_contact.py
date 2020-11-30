# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 08:26
# @Author  : 饭盆里
# @File    : test_contact.py
# @Software: PyCharm
# @desc    :
"""
待解决问题：
1. 打印  --done
2. department 类型为[] ,但传参是str的问题  (需要将步骤参数中的数据传递为list即可)
3. 串联逻辑断言校验
"""
import re

import pytest
from myinterface.company_wechart.page.contact_page import Wechart_contact


class TestContact():
    @pytest.mark.parametrize(('userid,name,mobile'), [("momo", 'momo', '13523232323')])
    def test_add_contact(self,userid,name,mobile):
        resjson = Wechart_contact().add_contact(userid, name, mobile)
        print(resjson)
        assert "created" == resjson['errmsg']
        return resjson

    @pytest.mark.parametrize('userid', [("FanPengLi")])
    def test_get_contact(self,userid):
        resjson = Wechart_contact().get_contact(userid)
        print(resjson)
        assert 'ok' == resjson['errmsg']
        return resjson

    @pytest.mark.parametrize('userid,name,mobile', [("momo", "momo", "18710000000")])
    def test_edit_contact(self,userid, name, mobile):
        resjson = Wechart_contact().edit_contact(userid, name, mobile)
        print(resjson)
        assert 'updated' == resjson['errmsg']
        return resjson

    @pytest.mark.parametrize('userid', [("momo")])
    def test_del_contact(self, userid):
        resjson = Wechart_contact().del_contact(userid)
        print(resjson)
        assert 'deleted' ==  resjson['errmsg']
        return resjson


    @pytest.mark.parametrize(('userid,name,mobile'), [("momo", 'momo', '13523232323')])
    def test_add_update_get_del_contact(self,userid,name,mobile):
        """
        业务串起来
        :return:
        """
        try:
            self.test_add_contact(userid,name,mobile)
        except Exception as e:
            if 'mobile existed' in e.__str__():
                # 将错误信息中的userid 提取出来，并AssertionError: assert 'created' == 'mobile existed:fanfan0'
                uu = re.findall(':(.*)\'',e.__str__())[0]
                self.test_del_contact(uu)
                self.test_add_contact(userid,name,mobile)
        self.test_get_contact(userid)
        self.test_edit_contact(userid,'fanfan',mobile)
        self.test_del_contact(userid)

