# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 11:26
# @Author  : 饭盆里
# @File    : test_datadrive.py
# @Software: PyCharm
# @desc    : 数据驱动的使用
import pytest
import yaml


class TestDatadrive():
    @pytest.mark.parametrize(('env'),yaml.safe_load(open('../data/env.yaml')))
    def test_env(self,env):
        print(env)
        if 'test' in env:
            print(f'这是测试环境，IP是{env["test"]}')
        elif 'dev' in env:
            print(f'这是开发环境，IP是{env["dev"]}')
        else:
            print('发生了什么？？')
