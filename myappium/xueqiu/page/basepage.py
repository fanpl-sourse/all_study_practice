# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:14
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
from time import sleep

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from myappium.xueqiu.tools.readyaml import Tools


class BasePage:
    """
    基础页面类
    """

    _blacklist = {(By.ID,'com.xueqiu.android:id/iv_close')}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self,by,locator=None):
        """
        查找元素
        :return:
        """
        try:
            if locator is None:
                element = self.driver.find_element(*by)
            else:
                element = self.driver.find_element(by,locator)
            return element

        except:
            for black in self._blacklist:
                elements = self.driver.find_elements(*black)
                if len(elements) >0:
                    elements[0].click()
            #递归调用，关闭弹框后，继续查找要找的元素
            return self.find(by,locator)



    def steps(self,steps_path,currentmethord):
        """
        解析操作步骤
        :param steps:   操作步骤文件的结果
        :param currentmethord:  当前测试的方法，比如进入主页面
        :return:
        """
        steps_list = Tools().read_yaml(steps_path)
        if currentmethord in steps_list.keys():
            #获取要测试方法的步骤列表
            steps = steps_list[currentmethord]
            for i in range(len(steps)):
                step = steps[i]
                if 'by' in step.keys() and 'locator' in step.keys():
                    if 'action' in step.keys():
                        if step['action'] == 'click':
                            self.find(step['by'],step['locator']).click()
                        elif step['action'] == 'key':
                            self.find(step['by'],step['locator']).send_keys(step['key'])

                if 'sleep' in step.keys():
                    sleep(step['sleep'])






