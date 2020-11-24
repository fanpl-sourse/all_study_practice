# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 20:00
# @Author  : 饭盆里
# @File    : test_schema.py
# @Software: PyCharm
# # @desc    :
import json
from jsonschema import validate
import requests

class TestSchema:
    def test_schema(self):
        url = 'https://testerhome.com/api/v3/topics.json'
        data = requests.get(url=url,params={"limit":"2"}).json()
        schema = json.load(open('topic_schema.json'))
        validate(data,schema=schema)


