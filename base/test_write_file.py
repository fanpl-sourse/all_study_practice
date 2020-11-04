# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 17:05
# @Author  : 饭盆里
# @File    : test_add_contact.py
# @Software: PyCharm
# @desc    :

import os

FILE_PATH = "/Users/a/Documents/2020study/all_study_practice/base/demo.txt"

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, encoding="utf-8", mode="w+") as FILE_HANDLER:
        for i in range(50000,60000):
            s = 'fanfantest_10N_50_'+str(i)+'\n'
            FILE_HANDLER.write(s)


