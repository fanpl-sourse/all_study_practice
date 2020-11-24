# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 08:43
# @Author  : 饭盆里
# @File    : test_demo.py
# @Software: PyCharm
# @desc    :

import requests

class TestDemo:
    def test_get(self):
        r = requests.get('https://api.github.com/repos/psf/requests')
        print(r)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_get1(self):
        """
        带有传参，关注结果中的args和 url的变化
        :return:
        """
        params ={
            "name":"hi",
            "password":"ha"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params=params)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        """
        关注结果中的form表单
        :return:
        """
        params = {
            "name": "hi",
            "password": "ha"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=params)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        """
        关注结果中的form表单
        :return:
        """
        params = {
            "name": "hi",
            "password": "ha"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=params)
        print(r.text)
        assert r.status_code == 200

    def test_post_file(self):
        """
        文件上传
        :return:
        """
        files = {'file':open('./test.txt','rb')}
        r = requests.post('http://httpbin.testing-studio.com/post',files=files)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        """
        header构造
        :return:
        """
        headers = {"name":"xix"}
        cookies = {"cookies":"axiba"}
        r = requests.get('http://httpbin.testing-studio.com/get',headers=headers,cookies=cookies)
        print(r.text)
        assert r.status_code ==200

    def test_header_cookie(self):
        """
        header构造
        :return:
        """
        headers = {
            "name":"xix",
            "Cookie":"axiba"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',headers=headers)
        print(r.text)
        assert r.status_code ==200
        assert r.json()['headers']['Name'] == "xix"

from requests.auth import HTTPBasicAuth
class Test_oauth():
    def test_oauth(self):
        r = requests.get('http://httpbin.testing-studio.com/basic-auth/test/123',
                         auth = HTTPBasicAuth("test","123"))
        print(r.text)
