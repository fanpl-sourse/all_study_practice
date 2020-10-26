# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 17:20
# @Author  : 饭盆里
# @File    : add_address_po.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddAddressPo:

    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def add_address(self,username,mobile):
        self.driver.find_element(By.NAME,'username').send_keys(username)
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys(username)
        self.driver.find_element(By.NAME,'mobile').send_keys(mobile)

        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()

