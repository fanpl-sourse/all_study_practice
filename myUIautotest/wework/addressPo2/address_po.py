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

from myUIautotest.wework.addressPo2.add_address_po import AddAddressPo
from myUIautotest.wework.basepage import BasePage


class AddressPo(BasePage):
    """
    通讯录PO
    """

    def  goto_add_address(self):
        """
        点击"添加按钮"进入添加地址页面
        :return:
        """
        def wait_until_nextpage_element_presence(x):
            """
            等待直到下一个页面的元素出现
            :return:
            """
            element_lens = len(self.finds(By.NAME,'username'))
            if element_lens <= 0:
                self.find(By.XPATH, '//*[@class="ww_operationBar"]/a[1]').click()
            return element_lens > 0

        #方法一：显示等待，行不通，因为元素已出现且可以点击，但是页面未加载完成引发的点击还是跳转不到下一步
        # self.webdriver_wait((By.CSS_SELECTOR, '.js_add_member:nth-child(2)'))
        #方法二： 睡眠等待，可以，但是要等待的时长不固定，所以不是最优解
        # sleep(4)
        #方法三：重写显示等待，思想：直到下一个页面的元素出现，才停止点击
        self.mywebdriver_wait(wait_until_nextpage_element_presence)

        return AddAddressPo(self._driver)