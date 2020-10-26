# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 17:04
# @Author  : 饭盆里
# @File    : address_po.py
# @Software: PyCharm
# @desc    :
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from myUIautotest.wework.addressPo.add_address_po import AddAddressPo


class AddressPo:
    """
    通讯录PO
    """
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def  goto_add_address(self):
        """
        点击"添加按钮"进入添加地址页面
        :return:
        """
        WebDriverWait(self.driver,5,0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.js_add_member:nth-child(2)')))
        self.driver.find_element(By.CSS_SELECTOR, '.js_add_member:nth-child(2)').click()
        return AddAddressPo(self.driver)