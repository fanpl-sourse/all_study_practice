# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 22:41
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    """
    PO 基类
    """

    _driver = None
    _base_url = ''

    def __init__(self,driver:WebDriver = None):
        if driver is  None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=option)

        else:
            self._driver = driver

        self._driver.implicitly_wait(3)

        if self._base_url != '':
            self._driver.get(self._base_url)

    def setup(self):
        pass

    def teardown(self):
        self._driver.quit()

    def find(self,by,locator=None):
        """
        重写self.driver.find_element() 函数，将driver相关的，都封装到basepage页面
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            result = self._driver.find_element(*by)
        else:
            result = self._driver.find_element(by,locator)

        return result

    def finds(self,by,locator):
        """
        发现多个元素
        :return:  元素个数
        """
        if locator is None:
            result = self._driver.find_elements(*by)
        else:
            result = self._driver.find_elements(by, locator)

        return result


    def webdriver_wait(self,locator):
        """
        显示等待
        :return:
        """
        WebDriverWait(self._driver, 5, 0.5).until(EC.element_to_be_clickable(locator))

    def mywebdriver_wait(self,condition):
        """
        重写显示等待，因为这个元素虽然在页面上出现了，但还是处于不可以点击的状态
        :return:
        """
        WebDriverWait(self._driver,10).until(condition)

