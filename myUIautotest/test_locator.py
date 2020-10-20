# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 09:40
# @Author  : 饭盆里
# @File    : test_locator.py
# @Software: PyCharm
# @desc    : 测试定位方式 https://www.cnblogs.com/fanpl/articles/9185051.html
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocator():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_Id(self):
        """
        打开百度首页，输入${hi}，点击【百度一下】进行检索
        :return:
        """
        self.driver.find_element(By.ID,'kw').send_keys('hi')
        self.driver.find_element(By.XPATH,'//*[@class="bg s_btn"]').click()
        sleep(2)

    def test_class(self):
        """
        打开百度首页，点击【设置】
        :return:
        """
        self.driver.find_element(By.CLASS_NAME,'c-color-t').click()
        sleep(2)

    def test_xpath(self):
        """
        打开百度首页中的新闻标签
        :return:
        """
        # self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[1]').click()
        print("使用属性")
        self.driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[@href="http://news.baidu.com"]').click()
        sleep(2)

    def test_text_link(self):
        """
        打开百度首页中的新闻标签 ，a标签，不建议使用这种定位方式
        :return:
        """
        self.driver.find_element_by_link_text('新闻').click()
        sleep(2)

