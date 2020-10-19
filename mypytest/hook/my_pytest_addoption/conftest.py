# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 09:29
# @Author  : 饭盆里
# @File    : conftest.py
# @Software: PyCharm
# @desc    : pytest_addoption
'''
解决问题： pytest命令行增加自定义参数
'''
import pytest
import yaml

# fixture函数 读入通过装饰器传入的参数
@pytest.fixture(autouse=True,params=['22222222','3333333333'])
def login(request):
    print('*'*100)
    print(request.param)

def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    """
        pytest 命令行添加自定义参数
        :param parser: 解析器
        :return:
        """
    # 设置一个group节点，group 将下面所有的option展示在这个group 下
    mygroup = parser.getgroup("fanpl")
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )

# 读入通过命令行传入的参数
@pytest.fixture(scope='session')
def read_envdata(request):
    """
    解析参数
    :param request:
    :return:
    """
    # 获取命令行入参参数
    myenv =  request.config.getoption('--env',default='test')

    try:
        if myenv == 'test':
            datapath = 'data/test/test_env.yaml'
        elif myenv == 'div':
            datapath = 'data/div/div_env.yaml'

        with open(datapath) as f:
            datas = yaml.safe_load(f)

        return myenv, datas
    except Exception as es:
        print(f'未知入参，请确保环境变量在 test/div 中,{es}')

