# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:14
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from myappium.xueqiu.tools.readyaml import Tools


class BasePage:
    """
    基础页面类
    """

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self,by,locator=None):
        """
        查找元素
        :return:
        """
        if locator is None:
            element = self.driver.find_element(*by)
        else:
            element = self.driver.find_element(by,locator)
        return element


    def steps(self,steps_path,currentstep):
        """
        解析操作步骤
        :param steps:   操作步骤文件的结果
        :param currentstep:  当前的步骤
        :return:
        """
        steps = Tools().read_yaml(steps_path)

        if currentstep in steps.keys():
            step = steps[currentstep]
            if 'by' in step.keys() and 'locator' in step.keys():
                if 'action' in step.keys():
                    if step['action'] == 'click':
                        self.find(step['by'],step['locator']).click()
                    elif step['action'] == 'key':
                        self.find(step['by'],step['locator']).send_keys(step['key'])






