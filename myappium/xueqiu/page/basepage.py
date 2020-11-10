# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 11:14
# @Author  : 饭盆里
# @File    : basepage.py
# @Software: PyCharm
# @desc    :
import json
from time import sleep

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from myappium.xueqiu.tools.handle_black import handle_black
from myappium.xueqiu.tools.readyaml import Tools


class BasePage:
    """
    基础页面类
    """

    _blacklist = {(By.ID,'com.xueqiu.android:id/iv_close'),
                  (By.ID,'com.xueqiu.android:id/ib_close')
                 }
    _black_error_max_num = 3
    _black_error_num =0

    #用于变量替换
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # def find(self,by,locator=None):
    #     """
    #     查找元素
    #     :return:
    #     """
    #     try:
    #         if locator is None:
    #             element = self.driver.find_element(*by)
    #         else:
    #             element = self.driver.find_element(by,locator)
    #
    #         self._black_error_num = 0
    #         return element
    #
    #     except Exception as e:
    #         if self._black_error_num >self._black_error_max_num:
    #             self._black_error_num = 0
    #             return e
    #         self._black_error_num += 1
    #         for black in self._blacklist:
    #             elements = self.driver.find_elements(*black)
    #             if len(elements) >0:
    #                 elements[0].click()
    #                 #递归调用，关闭弹框后，继续查找要找的元素
    #                 return self.find(by,locator)
    #
    #         raise ValueError('元素不在黑名单中')

    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """
        if locator is None:
            element = self.driver.find_element(*by)
        else:
            element = self.driver.find_element(by,locator)
        return element

    def finds(self,by,locator=None):
        if locator is None:
            element = self.driver.find_elements(*by)
        else:
            element = self.driver.find_elements(by, locator)
        return element

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

            string_steps = json.dumps(steps)
            for key, value in self._params.items():
                string_steps = string_steps.replace('${' + key + '}', value)

            steps = json.loads(string_steps)

            for i in range(len(steps)):
                step = steps[i]

                if 'by' in step.keys() and 'locator' in step.keys():
                    if 'action' in step.keys():
                        action = step['action']
                        if action == 'click':
                            self.find(step['by'],step['locator']).click()
                        elif action == 'sendkey':
                            self.find(step['by'],step['locator']).send_keys(step['value'])
                        elif action == 'len>0':
                            return len(self.finds(step['by'],step['locator'])) >0

                if 'sleep' in step.keys():
                    sleep(step['sleep'])






