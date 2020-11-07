# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:25
# @Author  : 饭盆里
# @File    : main_page.py
# @Software: PyCharm
# @desc    :
import os
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from myappium.xueqiu.page.basepage import BasePage
from myappium.xueqiu.page.search_page import SearchPage


class MainPage(BasePage):
    """
    雪球APP主页面
    """
    # search_element = (By.ID,'com.xueqiu.android:id/tv_search')
    # pen_sheep_element = (By.ID,'com.xueqiu.android:id/post_status')

    def goto_search_page(self):
        """
        进入检索页面
        :return:
        """
        # self.find(self.search_element).click()
        # print(os.getcwd())
        self.steps('../page_steps/main_page_step.yaml','goto_search_page')

        return SearchPage(self.driver)

    def goto_black_then_goto_search(self):
        """
        先通过笔符进入类似弹框的黑名单页，然后退出，并进入到检索页面
        :return:
        """
        # self.find(self.pen_sheep_element).click()
        # sleep(2)
        # self.find(self.search_element).click()
        self.steps('../page_steps/main_page_step.yaml', 'goto_black_then_goto_search')
        return SearchPage(self.driver)
