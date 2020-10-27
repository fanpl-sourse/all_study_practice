# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 15:31
# @Author  : 饭盆里
# @File    : test_thefirstscript.py
# @Software: PyCharm
# @desc    : 验证一下环境

# from selenium import webdriver
# from time import sleep
#
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# sleep(2)
# driver.quit()

cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False},{'domain': '.work.weixin.qq.com', 'httpOnly': False}]
for cookie in cookies:
    print(cookie)
    if 'httpOnly' in cookie.keys():
        cookie.pop('httpOnly')
    print("*"*10)
    print(cookie)

