# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 15:26
# @Author  : 饭盆里
# @File    : login_po.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from myUIautotest.wework.homePo.register_po import RegistorPo


class LoginPo:
    def __init__(self,driver:WebDriver):
        self.driver = driver


    def scan_login(self):
        """
        扫码登录
        :return:
        """


    def goto_register(self):
        """
        进入企业注册
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return RegistorPo(self.driver)