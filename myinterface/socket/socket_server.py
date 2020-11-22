# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 11:15
# @Author  : 饭盆里
# @File    : socket_server.py
# @Software: PyCharm
# @desc    :

import socket

#创建socket对象
s = socket.socket()
#绑定端口
s.bind(('127.0.0.1',12345))

#等待客户端连接
s.listen(5)

while True:
    #建立客户端连接
    c,addr = s.accept()
    print("连接地址",addr)
    c.send('你好'.encode())
    c.close()
