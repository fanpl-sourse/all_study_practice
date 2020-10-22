# -*- coding: utf-8 -*-
# @Time    : 2020/10/19 18:43
# @Author  : 饭盆里
# @File    : test_wait.py
# @Software: PyCharm
# @desc    : 测试各种等待
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def  setup(self):
        print('*'*20+'setup'+'*'*20)
        self.driver  = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        print('*'*20+'teardown'+'*'*20)
        self.driver.quit()

    def testsleep(self):
        print('hi')
        sleep(2)
        print('使用sleep等待了2s')

    def test_implicitly_wait(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()

    def test_webdriverwait(self):
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        element = WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.ID,'su')))
        element.click()

class TestWebdriverwait():
    def setup(self):
        print('*' * 20 + 'setup' + '*' * 20)
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        self.driver.maximize_window()

    def teardown(self):
        print('*'*20+'teardown'+'*'*20)
        self.driver.quit()

    def test_webdriverwait2(self):
        self.driver.find_element(By.XPATH,'//*[@id="main-nav-menu"]/ul/li[3]/a').click()
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[@id="main"]/div/div[1]/div[1]/div[1]/ul/li[2]/a')) >1
        WebDriverWait(self.driver,5,0.5).until(wait)
        print('后续操作')

    def test_webdriverwait3(self):
        self.driver.find_element(By.XPATH,'//*[@id="main-nav-menu"]/ul/li[3]/a').click()
        WebDriverWait(self.driver,5,0.5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="main"]/div/div[1]/div[1]/div[1]/ul/li[2]/a')))
        print('后续操作')






