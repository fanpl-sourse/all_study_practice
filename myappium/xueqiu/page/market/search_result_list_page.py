# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 10:34
# @Author  : 饭盆里
# @File    : search_result_list_page.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from myappium.xueqiu.page.basepage import BasePage


class SearchResultListPage(BasePage):
    def add_mychoice(self,stock_num):
        """
        添加自选
        :return:
        """
        self._params['stock_num'] = stock_num
        self.steps('../page_steps/market/search_result_list_page_step.yaml','add_mychoice')
        # self.find(By.XPATH,'//*[@text="09988"]/../../..//*[@text="加自选"]').click()
        return self

    def assert_add_mychoice_success(self,stock_num):
        """
        断言添加自选成功
        :return:
        """
        self._params['stock_num'] = stock_num
        # element = self.finds(By.XPATH,'//*[@text="09988"]/../../..//*[@text="已添加"]')
        # assert len(element) >0
        assert self.steps('../page_steps/market/search_result_list_page_step.yaml', 'assert_add_mychoice_success')
