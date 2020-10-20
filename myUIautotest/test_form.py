# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 17:50
# @Author  : 饭盆里
# @File    : test_form.py
# @Software: PyCharm
# @desc    : form 表单
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/account/sign_in')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        """
        1. 打开testhome登录地址
        2. 输入用户名
        3. 输入密码
        4. 点击‘记住’标签
        5. 点击登录，提交表单
        :return:
        """
        self.driver.find_element(By.XPATH,'//*[@id="user_login"]').send_keys('ff')
        self.driver.find_element(By.XPATH,'//*[@type="password"]').send_keys('11')
        self.driver.find_element(By.ID,'user_remember_me').click()
        self.driver.find_element(By.NAME,'commit').click()
        sleep(2)


