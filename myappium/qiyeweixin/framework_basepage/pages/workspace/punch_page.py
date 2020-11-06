# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 08:38
# @Author  : 饭盆里
# @File    : punch_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage


class PunchPage(BasePage):
    """
    打卡页面
    """

    outside_punch_element = (MobileBy.ID, 'com.tencent.wework:id/gw8')
    punch_button_element = (MobileBy.ID, 'com.tencent.wework:id/ao_')
    punch_success_element = (MobileBy.XPATH, '//*[contains(@text,"打卡成功")]')

    def switchto_outside_punch(self):
        """
        切换到外出打卡
        :return:
        """
        # 切换到【外出打卡】
        self.find_and_click(self.outside_punch_element)
        return self

    def outside_punch(self):
        """
        外出打卡
        :return:
        """
        # 选中打开范围，点击
        self.find_and_click(self.punch_button_element)
        return self

    def assert_punch_success(self):
        """
        断言打点成功
        :return:
        """
        # 断言
        assert_content = self.find(self.punch_success_element).text
        assert "打卡成功" in assert_content