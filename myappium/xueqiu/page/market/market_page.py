# -*- coding: utf-8 -*-
# @Time    : 2020/11/8 10:23
# @Author  : 饭盆里
# @File    : market_page.py
# @Software: PyCharm
# @desc    :
import os

from selenium.webdriver.common.by import By
from myappium.xueqiu.page.basepage import BasePage
from myappium.xueqiu.page.market.search_stock_page import SearchStockPage
from myappium.xueqiu.tools.readyaml import Tools


class MarketPage(BasePage):
    """
    行情页面
    """
    def goto_search_stock(self):
        """
        进入搜索股票页面
        :return:
        """
        # self.find(By.XPATH,'//*[@class="android.widget.TextView" and @text="行情"]').click()
        self.steps('../page_steps/market/market_page_step.yaml','goto_search_stock')
        return SearchStockPage(self.driver)