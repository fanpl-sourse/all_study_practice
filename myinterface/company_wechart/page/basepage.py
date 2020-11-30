# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 08:44
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
"""
基础页面：
1. 将requests封装起来
2. 替换变量
"""
import json

import requests


class BasePage:
    _params = {}

    def send(self,data):
        # {'method': 'post', 'url': 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=${token}', 'json': {'userid': '${userid}', 'name': '${name}', 'mobile': '${mobile}', 'department': '${department}'}}

        #######替换${}为变量值
        #将dict转为str
        data = json.dumps(data)
        for key,value in self._params.items():
            data = data.replace('${'+key+'}',value)

        data = json.loads(data)
        return requests.request(**data).json()
