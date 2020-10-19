# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 11:18
# @Author  : 饭盆里
# @File    : conftest.py.py
# @Software: PyCharm
# @desc    : pytest_generate_tests 实现自定义动态参数方案
"""
等同于：在测试用例上面增加
       @pytest.mark.parametrize()
"""

#通过方法动态生成测试用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas,  # 获取当前测试数据
                             ids=metafunc.module.myids,
                             scope='function')