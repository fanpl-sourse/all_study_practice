# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 15:13
# @Author  : 饭盆里
# @File    : test_actionchains.py
# @Software: PyCharm
# @desc    : actionChains PC 端鼠标操作
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        """
        模拟点击、双击、右键操作
        :return:
        """
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        cl = self.driver.find_element(By.CSS_SELECTOR,'[onclick="cl(event)"]')
        dbl = self.driver.find_element(By.XPATH,'//input[@ondblclick="dcl(event)"]')
        rl = self.driver.find_element(By.XPATH,'/html/body/form/input[4]')

        action = ActionChains(self.driver)
        action.click(cl)
        action.double_click(dbl)
        action.context_click(rl)
        sleep(2)
        action.perform()

    def test_move_mouth(self):
        """
        移动到元素上
        :return:
        """
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

        baidusetting = self.driver.find_element(By.ID,'s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(baidusetting)
        action.perform()

    def test_drag_and_drop(self):
        """
        把一个元素拖拽到另一个元素
        :return:
        """
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        drag = self.driver.find_element(By.ID,'dragger')
        drop = self.driver.find_element(By.XPATH,'/html/body/div[4]')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop)
        action.perform()
        sleep(3)

    def test_drag_and_drop1(self):
        """
        把一个元素拖拽到另一个元素: 按下-拖走-释放
        :return:
        """
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        drag = self.driver.find_element(By.ID,'dragger')
        drop = self.driver.find_element(By.XPATH,'/html/body/div[4]')

        action = ActionChains(self.driver)

        action.click_and_hold(drag)
        action.move_to_element(drop)
        action.release()

        action.perform()
        sleep(3)

    def test_drag_and_drop2(self):
        """
        把一个元素拖拽到另一个元素: 按下保持 - 到某个元素释放
        :return:
        """
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

        drag = self.driver.find_element(By.ID,'dragger')
        drop = self.driver.find_element(By.XPATH,'/html/body/div[4]')

        action = ActionChains(self.driver)

        action.click_and_hold(drag)
        action.release(drop)

        action.perform()
        sleep(3)

    def test_keys(self):
        """
        ActionChains按键相关内容
        1. 输入内容hi~
        2. 回退一个字符
        3. 追加 tom
        4. 清空
        :return:
        """
        self.driver.get('http://sahitest.com/demo/label.htm')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        username = self.driver.find_element(By.XPATH,'/html/body/label[1]/input')

        action = ActionChains(self.driver)

        action.send_keys_to_element(username,'hi~')
        action.send_keys_to_element(username,Keys.BACKSPACE).pause(1)
        action.send_keys_to_element(username,Keys.BACKSPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys_to_element(username,Keys.CLEAR).pause(1)

        action.perform()
        sleep(2)

    def test_keys1(self):
        """
        ActionChains按键相关内容
        1. 输入内容hi~
        2. 回退一个字符
        3. 追加 tom
        4. 清空
        :return:
        """
        self.driver.get('http://sahitest.com/demo/label.htm')
        self.driver.find_element_by_xpath('/html/body/label[1]/input').click()

        action = ActionChains(self.driver)
        action.send_keys('hi ~').pause(1)
        action.send_keys(Keys.BACKSPACE).pause(1)
        action.send_keys('你好吗？').pause(1)
        action.send_keys(Keys.CLEAR).pause(1)
        action.perform()
        sleep(2)
