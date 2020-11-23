# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 10:12
# @Author  : 饭盆里
# @File    : test_pystache.py
# @Software: PyCharm
# @desc    : 使用模版
import pystache
import requests


class TestPystache():
    def test_pystache(self):
        print(pystache.render('Hi {{person}}!', {'person': 'Mom'}))

    def test_post_json(self):
        """
        关注结果中的form表单
        :return:
        """
        param = {
            'name': 'fff',
            'password':'123'
        }
        # params =  pystache.render('"name": {{name}},"password": {{password}}',param )
        with open('./test.txt','r') as f:
            params =  pystache.render(f.read(),param)

        r = requests.post('http://httpbin.testing-studio.com/post', json=params)
        print(r.text)
        assert r.status_code == 200