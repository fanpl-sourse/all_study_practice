# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 14:16
# @Author  : 饭盆里
# @File    : readyaml.py
# @Software: PyCharm
# @desc    :
import os

import yaml


class Tools:
    """
    主要包含一些工具
    """
    def read_yaml(self,dir):
        with open(dir) as f:
           data = yaml.safe_load(f)

           return data

if __name__ == '__main__':
    print(os.getcwd())
    print(Tools().read_yaml('./xueqiu/page_steps/main_page_step.yaml'))
