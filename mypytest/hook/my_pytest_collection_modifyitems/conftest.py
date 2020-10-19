# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 20:11
# @Author  : 饭盆里
# @File    : conftest.py.py
# @Software: PyCharm
# @desc    : hook 函数之 pytest_collection_modifyitems
'''
解决问题：
   自定义用例的执行顺序
   解决编码问题(中文的测试用例名称)
   自动添加标签
'''
from typing import List

import pytest


# @pytest.fixture(autouse=True)
# def login():
#     print('login')

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    '''
    :param session:
    :param config:
    :param items:  收集用例的列表
    :return:
    '''
    print(items)
    print(len(items))
    print("*"*30+'#'*30)
    #测试用例逆序
    items.reverse()

    #ids中中文乱码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # item.nodeid: 用例名称, 带标记运行
        if '1' in item.nodeid:
            item.add_marker(pytest.mark.first)
        if '2' in item.nodeid:
            item.add_marker(pytest.mark.second)






