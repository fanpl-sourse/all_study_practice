# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 15:35
# @Author  : 饭盆里
# @File    : test_company_wechart_contact.py
# @Software: PyCharm
# @desc    :
import requests


class Test_company_wechart_contact:

    def get_token(self):
        params = {
            "corpid":"ww9141708bbda1c588",
            "corpsecret":"F_AGdOLLFROJupVo2-H6WGjg8SErlDPb4OBVTsUlOp4"
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',params=params)
        access_token = r.json()['access_token']
        return access_token

    def test_add_contact(self):
        """
        添加联系人
        :return:
        """
        access_token = self.get_token()
        params = {
            "userid": "fanfan1",
            "name": "fanfan1",
            "mobile": "18700000000",
            "department": [1]
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}',json=params)
        print(r.json())

    def test_get_contact(self):
        """
        获取联系人
        :return:
        """
        access_token = self.get_token()
        params = {
            "access_token": access_token,
                 "userid":"fanfan1"
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/get',params=params)
        print(r.json())

    def test_edit_contact(self):
        """
        更新联系人
        :return:
        """
        access_token = self.get_token()
        jsondata={
            "userid": "fanfan1",
            "name": "ff1",
            "mobile": "18710000000"
        }
        r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}',json=jsondata)
        print(r.json())

    def test_del_contact(self):
        """
        删除联系人
        :return:
        """
        params = {
            "access_token":self.get_token(),
                 "userid":"fanfan1"
        }
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/delete',params=params)
        print(r.json())