# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 17:56
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
import logging

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """
    基础页面，封装driver、查找元素、点击、等待 等动作
    """

    logging.basicConfig(level=logging.INFO)
    def __init__(self,driver:WebDriver=None):
        """
        初始化driver
        因为各个页面都需要进行初始化的动作，所以把它提取出来放到父类basepage的__init__中，这样每个继承的都会运行这个动作
        """
        self.driver = driver

    def find(self,locator):
        """
        查找元素
        :return:
        """
        logging.info(f'查找元素：{locator}')
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
        """
        查看元素并进行点击
        :param locator:
        :return:
        """
        logging.info(f'查找元素并点击:{locator}')
        self.find(locator).click()


    def find_by_scroll(self,text):
        """
        通过滚动查找元素
        :param text:
        :return:
        """
        logging.info(f'滚动查找元素：{text}')
        return self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{text}").instance(0))').click()

    def webdriver_wait(self,locator,timeout):
        '''
        显示等待
        :return:
        '''
        element = WebDriverWait(self.driver,timeout).until(
            lambda x:x.find_element(*locator))
        return element

    def back(self,num=1):
        for i in range(num):
            self.driver.back()