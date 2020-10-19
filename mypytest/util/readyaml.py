# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 15:55
# @Author  : 饭盆里
# @File    : readyaml.py
# @Software: PyCharm
# @desc    : 读取yaml文件，返回文件内容
import yaml


class Util():
    def readyaml(self,path):
        return yaml.safe_load(open(path))
