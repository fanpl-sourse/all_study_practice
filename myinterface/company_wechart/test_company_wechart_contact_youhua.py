# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 15:35
# @Author  : 饭盆里
# @File    : test_company_wechart_contact.py
# @Software: PyCharm
# @desc    :
"""
【优化】
token 放到 fixture，从而实现只调用一次就可以多个地方使用token
断言：整体逻辑
           1. 新增时，如果存在，则删除再新增，新增后用获取接口验证

           2. 删除时，删除后用获取接口验证

入参参数化
"""
import re

import pytest
import requests

##生成数据
def contact_data():
    data = [ ('fanfan'+str(i),'fanfan'+str(i),'18799%06d'%i)
             for i in range(10)]
    print(data)
    return data

class Test_company_wechart_contact:
    @pytest.fixture(scope='session')
    def token(self):
        params = {
            "corpid": "ww9141708bbda1c588",
            "corpsecret": "F_AGdOLLFROJupVo2-H6WGjg8SErlDPb4OBVTsUlOp4"
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        return r.json()['access_token']

    @pytest.mark.parametrize('userid,name,mobile',contact_data())
    def test_add_contact(self,token,userid,name,mobile,department=None):
        """
        添加联系人
        :return:
        """
        if department is None:
            department = [1]
        params = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}',json=params)
        return  r.json()
        # assert 'created'  == r.json()['errmsg']


    @pytest.mark.parametrize('userid',[("fanfan1"),("fanfan0")])
    def test_get_contact(self,token,userid):
        """
        获取联系人
        :return:
        """
        params = {
            "access_token": token,
                 "userid":userid
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/get',params=params)
        print(r.json())
        assert 'ok' in r.json()['errmsg']

    @pytest.mark.parametrize('userid,name,mobile',[("fanfan1","ff1","18710000000")])
    def test_edit_contact(self,token,userid,name,mobile):
        """
        更新联系人
        :return:
        """
        jsondata={
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}',json=jsondata)
        print(r.json())
        assert 'updated' == r.json()['errmsg']

    @pytest.mark.parametrize('userid',[("fanfan0")])
    def test_del_contact(self,token,userid):
        """
        删除联系人
        :return:
        """
        params = {
            "access_token":token,
                 "userid":userid
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/delete',params=params)
        print(r.json())
        assert 'deleted' == r.json()['errmsg']

    @pytest.mark.parametrize(('userid,name,mobile'), contact_data())
    def test_add_update_get_del_contact(self,token,userid,name,mobile):
        """
        业务串起来
        :return:
        """
        try:
            assert 'created' ==  self.test_add_contact(token,userid,name,mobile)['errmsg']
        except Exception as e:
            if 'mobile existed' in e.__str__():
                # 将错误信息中的userid 提取出来，并AssertionError: assert 'created' == 'mobile existed:fanfan0'
                uu = re.findall(':(.*)\'',e.__str__())[0]
                self.test_del_contact(token,userid)
                self.test_add_contact(token,userid,name,mobile)
        self.test_get_contact(token,userid)
        self.test_edit_contact(token,userid,'fanfan',mobile)
        self.test_del_contact(token,userid)