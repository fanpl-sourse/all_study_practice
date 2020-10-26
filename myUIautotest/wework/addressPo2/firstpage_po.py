# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 16:56
# @Author  : 饭盆里
# @File    : firstpage_po.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from myUIautotest.wework.addressPo2.address_po import AddressPo
from myUIautotest.wework.basepage import BasePage


class FirstPagePo(BasePage):
    """
    首页PO
    """
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_address(self):
        """
        进入通讯录PO
        :return:
        """
        self.find(By.CSS_SELECTOR,'#menu_contacts').click()

        return AddressPo(self._driver)