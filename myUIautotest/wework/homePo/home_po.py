# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 15:22
# @Author  : 饭盆里
# @File    : home_po.py
# @Software: PyCharm
# @desc    :
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from myUIautotest.wework.homePo.login_po import LoginPo
from myUIautotest.wework.homePo.register_po import RegistorPo


class HomePo:
    """
    企业微信首页PO
    """

    def __init__(self):
        option = Options()
        option.debugger_address='127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(3)

    def goto_login(self):
        """
        进入企业登录
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPo(self.driver)

    def goto_register(self):
        """
        进入立即注册
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return RegistorPo(self.driver)