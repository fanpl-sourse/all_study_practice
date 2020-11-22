# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 11:18
# @Author  : 饭盆里
# @File    : sockte_client.py
# @Software: PyCharm
# @desc    :
import socket

s =socket.socket()
s.connect(("127.0.0.1",12345))
print('hello')
print(s.recv(1024).decode())
s.close()