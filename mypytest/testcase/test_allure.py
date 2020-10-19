# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 16:31
# @Author  : 饭盆里
# @File    : test_pytest.py
# @Software: PyCharm
# @desc    : allure 练习
import allure
import pytest
import yaml


def func(x):
    return x + 1

@pytest.fixture()
def login():
    print('login')
    return 'login'

@allure.feature('测试功能模块')
class TestFunc:

    @pytest.mark.parametrize(('a,b'), yaml.safe_load(open('../data/alluredata.yml')))
    def test_yaml(self, a, b):
        assert func(a) == b

    @allure.story('参数化')
    @pytest.mark.parametrize(['a','b'],[
        (1,2),
        (2,3),
        (3,4)
    ])
    def test_func(self,a,b):
        assert func(a) == b

    @allure.story('使用了fixture 函数')
    def test_b(self,login):
        print(f'test_b:{login}')
    
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('step练习')
    @allure.testcase('https://www.baidu.com','测试用例1---step练习')
    @allure.title('step练习')
    def test_step(self):
        with allure.step('这是第一步'):
            print('step1')

        with allure.step('这是第二步'):
            print('第二步')

        allure.attach.file('/Users/a/Pictures/1.jpg',name='图片',attachment_type=allure.attachment_type.PNG)
        print('hi')





