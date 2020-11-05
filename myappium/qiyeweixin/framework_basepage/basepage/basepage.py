# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 17:56
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.android.webdriver import WebDriver
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

    def find_and_sendkeys(self,locator,key):
        """
        查看元素并键入值
        :param locator:
        :return:
        """
        logging.info(f'查找元素并点击:{locator},输入的值：{key}')
        self.find(locator).send_keys(key)

    def find_elements_by_text(self,text):
        """
        通过文本信息查找元素列表
        :param text:
        :return:
        """
        logging.info(f'通过文本信息{text}查找元素列表')
        return self.driver.find_elements(MobileBy.XPATH, f'//*[@text="{text}"]')


    def find_by_scroll(self,text):
        """
        通过滚动查找元素
        :param text:
        :return:
        """
        logging.info(f'滚动查找元素：{text}')
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 f'new UiScrollable(new UiSelector().scrollable(true).instance(0))'
                                 f'.scrollIntoView(new UiSelector().text("{text}").instance(0))').click()

    def clear_input(self,locator):
        """
        清空输入框
        :return:
        """
        logging.info(f"清空输入框内容:{locator}")
        self.driver.find_element(*locator).clear()

    def webdriver_wait(self,locator,timeout):
        '''
        显示等待
        :return:
        '''
        element = WebDriverWait(self.driver,timeout).until(
            lambda x:x.find_element(*locator))
        return element

    def back(self,num=1):
        """
        返回次数
        :param num:
        :return:
        """
        logging.info(f'返回次数：{num}')
        for i in range(num):
            self.driver.back()



