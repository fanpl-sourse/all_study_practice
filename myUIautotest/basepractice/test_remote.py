# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 19:43
# @Author  : 饭盆里
# @File    : test_remote.py
# @Software: PyCharm
# @desc    : 复用浏览器
"""
应用场景：
在调试的过程中，需要每次都从头开始运行，这导致需要等待时间过长，或者卡在扫码登录的地方，无法进行下去
为了实现避免从头开始调试，可以采用复用浏览器
具体操作：
1. 在已有的Chrome上打开调试 (可执行文件名 chrome.exe)
2. 修改selenium代码，让她适应这种调试
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




class TestRemote():
    def setup(self):

        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启调试，
        # 由于我环境变量设置了变量，alias driver_debugging='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222'
        # 所以可以直接：driver_debugging
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        self.driver.quit()

    def test_remote_debug(self):
        self.driver.find_element(By.ID,'menu_contacts').click()
        sleep(2)



