# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 08:22
# @Author  : 饭盆里
# @File    : util.py
# @Software: PyCharm
# @desc    : 工具类
import requests
import yaml
from myinterface.company_wechart.page.basepage import BasePage


class Util(BasePage):

    def token(self):
        # params = {
        #     "corpid": "ww9141708bbda1c588",
        #     "corpsecret": "F_AGdOLLFROJupVo2-H6WGjg8SErlDPb4OBVTsUlOp4"
        # }
        # r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # return r.json()['access_token']

        data = yaml.safe_load(open('../pagesteps/util_steps.yaml'))['token']
        return self.send(data)['access_token']