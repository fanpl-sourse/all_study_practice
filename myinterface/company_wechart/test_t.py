# -*- coding: utf-8 -*-
# @Time    : 2020/11/28 21:52
# @Author  : 饭盆里
# @File    : test_t.py
# @Software: PyCharm
# @desc    :
import json
import re

import yaml


def test_t():
    st = "assert 'created' == 'mobile existed:fanfan0'"
    s = re.findall(':(.*)\'', st)
    print(s[0])

def test_d():
    a = {"f":"hihi","p":"haha"}
    #解元祖
    def t(**a):
        print(a)

    t(**a)
    t(f="hihi",p="hhaha")

def test_e():

    def send(data):
        print(data)
        print(type(data))
    data = {
        "method": "post",
        "url": f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token',
        "jsondata": {
            "userid": "hihi"
        }
    }

    send(data)

def test_read():
    data = yaml.safe_load(open('./pagesteps/contact_page_steps.yaml'))['add_contact']
    print(data)
    return data



def test_change():
    a = {"name":"fan"}
    st = "i am ${name}"
    for key,value in a.items():
        new_st = st.replace("${"+key+"}",value)
    print(new_st)

def test_read_change():
    department = "1"
    a={"token":"1234","name":"xixi","mobile":"18799999999","userid":"111","department":department}
    dic = test_read()
    # dic-->>str
    st = json.dumps(dic)
    for key,value in a.items():
        st = st.replace("${"+key+"}",value)
    print(st)

