# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 10:27
# @Author  : 饭盆里
# @File    : search_stock_page_step.yaml.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By

from myappium.xueqiu.page.basepage import BasePage
from myappium.xueqiu.page.market.search_result_list_page import SearchResultListPage


class SearchStockPage(BasePage):
    def search_stock(self,stock_name,stock_num):
        """
        检索股票
        :return:
        # """
        # #点击检索符号
        # self.find(By.ID,'com.xueqiu.android:id/action_search').click()
        # #输入检索内容
        # self.find(By.ID,'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        # #选择内容点击
        # self.find(By.XPATH,'//*[@text="09988"]').click()

        self._params['stock_name'] = stock_name
        self._params['stock_num'] = stock_num
        self.steps('../page_steps/market/search_stock_page_step.yaml','search_stock')

        return SearchResultListPage(self.driver)

