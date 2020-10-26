# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 16:56
# @Author  : 饭盆里
# @File    : firstpage_po.py
# @Software: PyCharm
# @desc    :
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from myUIautotest.wework.addressPo.address_po import AddressPo


class FirstPagePo:
    """
    首页PO
    """
    def __init__(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.implicitly_wait(3)

    def goto_address(self):
        """
        进入通讯录PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'#menu_contacts').click()

        return AddressPo(self.driver)