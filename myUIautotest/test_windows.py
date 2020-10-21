# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 19:48
# @Author  : 饭盆里
# @File    : test_windows.py
# @Software: PyCharm
# @desc    : 多窗口切换
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWindows():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_windows(self):
        """
        打开百度
        点击登录
        弹框中点击"立即注册"，输入账户和密码
        返回登录页，点击登录
        输入用户名密码，点击登录
        :return:
        """
        self.driver.find_element(By.XPATH,'//*[@id="u1"]/a').click()
        self.driver.find_element_by_link_text('立即注册').click()
        windows = self.driver.window_handles

        self.driver.switch_to.window(windows[1])
        self.driver.find_element(By.NAME,'userName').send_keys('fff')
        self.driver.find_element(By.NAME,'phone').send_keys('18700000000')
        sleep(1)

        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__footerULoginBtn').click()
        sleep(1)
        self.driver.find_element(By.NAME,'userName').send_keys('fff')
        sleep(1)
        self.driver.find_element(By.NAME,'password').send_keys('111111')
        sleep(1)
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__submit').click()

        sleep(3)

