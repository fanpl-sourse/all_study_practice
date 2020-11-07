# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:28
# @Author  : 饭盆里
# @File    : search_page.py
# @Software: PyCharm
# @desc    :
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from myappium.xueqiu.page.basepage import BasePage
from myappium.xueqiu.page.search_result_page import SearchResultPage


class SearchPage(BasePage):

    # search_and_sendkey_element = (MobileBy.ID,'com.xueqiu.android:id/search_input_text')

    """
    检索页面
    """
    def goto_search_result_page(self,value):
        """
        进入检索结果页面
        :return:
        """
        # self.find(self.search_and_sendkey_element).send_keys(value)
        self.steps('../page_steps/search_page_steps.yaml','goto_search_result_page')
        sleep(3)
        return SearchResultPage(self.driver)