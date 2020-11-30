# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 08:20
# @Author  : 饭盆里
# @File    : contact_page.py
# @Software: PyCharm
# @desc    :
"""
优化
1. 用例与api分开
2. 将fixture中的token方法，提取到工具类中，并在__init__方法中引入，因为别的位置也会使用
3. 将requests封装起来，用send方法发送所有的requests请求，为操作 和 步骤入参数据分离做准备
4. 将步骤入参数据放到yaml文件中

"""
import pytest
import requests
import yaml

from myinterface.company_wechart.page.basepage import BasePage
from myinterface.company_wechart.page.util import Util

class Wechart_contact(BasePage):

    def __init__(self):
        self.token = Util().token()
        self._params['token'] = self.token

    def add_contact(self,userid,name,mobile,department=None):
        """
        添加联系人
        :return:
        """
        # if department is None:
        #     department = [1]
        # params = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": department
        # }
        # r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}',json=params)
        # return r.json()


        # if department is None:
        #     department = [1]
        # data = {
        #     "method":"post",
        #     "url": f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}',
        #     "json": {
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department
        #     }
        # }
        # return self.send(data)


        department = '1'
        self._params['userid'] = userid
        self._params['name'] = name
        self._params['mobile'] = mobile
        self._params['department'] = department
        data = yaml.safe_load(open('../pagesteps/contact_page_steps.yaml'))['add_contact']
        return self.send(data)


    def get_contact(self,userid):
        """
        获取联系人
        :return:
        """
        # params = {
        #     "access_token": self.token,
        #          "userid":userid
        # }
        # r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/get',params=params)
        # return r.json()

        # data = {
        #     "method":"get",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/user/get",
        #     "params":{
        #         "access_token": self.token,
        #         "userid": userid
        #     }
        # }
        # return self.send(data)

        self._params['userid'] = userid
        data = yaml.safe_load(open('../pagesteps/contact_page_steps.yaml'))['get_contact']
        return self.send(data)


    def edit_contact(self,userid,name,mobile):
        """
        更新联系人
        :return:
        """
        # jsondata={
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile
        # }
        # r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}',json=jsondata)
        # return r.json()

        # data={
        #     "method":"post",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json":{
        #        "userid": userid,
        #        "name": name,
        #        "mobile": mobile
        #     }
        # }
        # return self.send(data)

        self._params['userid'] = userid
        self._params['name'] = name
        self._params['mobile'] = mobile

        data = yaml.safe_load(open('../pagesteps/contact_page_steps.yaml'))['edit_contact']
        return self.send(data)



    def del_contact(self,userid):
        """
        删除联系人
        :return:
        """
        # params = {
        #     "access_token":self.token,
        #          "userid":userid
        # }
        # r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/user/delete',params=params)
        # return r.json()

        # data = {
        #     "method":"get",
        #     "url":"https://qyapi.weixin.qq.com/cgi-bin/user/delete",
        #     "params":{
        #         "access_token":self.token,
        #         "userid":userid
        #     }
        # }
        # return self.send(data)

        self._params['userid'] = userid
        data = yaml.safe_load(open('../pagesteps/contact_page_steps.yaml'))['del_contact']
        return self.send(data)
