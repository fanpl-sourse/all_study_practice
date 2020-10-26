# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 17:20
# @Author  : 饭盆里
# @File    : add_address_po.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from myUIautotest.wework.basepage import BasePage

class AddAddressPo(BasePage):
    """
        新增通讯录页面
    """
    def add_address(self,username,mobile):
        self.find(By.NAME,'username').send_keys(username)
        self.find(By.ID,'memberAdd_acctid').send_keys(username)
        self.find(By.NAME,'mobile').send_keys(mobile)

        self.find(By.CSS_SELECTOR,'.js_btn_save').click()

