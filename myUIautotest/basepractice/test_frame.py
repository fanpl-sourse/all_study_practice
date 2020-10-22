# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 08:43
# @Author  : 饭盆里
# @File    : test_frame.py
# @Software: PyCharm
# @desc    : frame
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestFrame():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        """
        链接：https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        步骤：
            1. 在左边点击运行操作
            2. 在右边拖拽：拖拽我后
            3. 在左边点击运行操作
        :return:
        """
        self.driver.find_element(By.ID,'submitBTN').click()
        self.driver.switch_to.frame('iframeResult')

        action = ActionChains(self.driver)
        drag = self.driver.find_element(By.ID, 'draggable')
        drop = self.driver.find_element(By.ID,'droppable')
        action.drag_and_drop(drag,drop)
        action.perform()
        sleep(2)

        self.driver.switch_to.alert.accept()
        sleep(2)

        self.driver.switch_to.default_content()

        self.driver.find_element(By.ID,'submitBTN').click()
        sleep(2)