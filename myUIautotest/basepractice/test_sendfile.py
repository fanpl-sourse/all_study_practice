# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 08:31
# @Author  : 饭盆里
# @File    : test_sendfile.py
# @Software: PyCharm
# @desc    : 文件上传
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSendfile():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_sendfile(self):
        self.driver.find_element(By.XPATH,'//*[@class="soutu-btn"]').click()
        self.driver.find_element(By.XPATH,'//*[@class="upload-pic"]').send_keys('/Users/a/Pictures/1.jpg')
        sleep(3)