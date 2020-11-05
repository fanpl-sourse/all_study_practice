# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 08:59
# @Author  : 饭盆里
# @File    : search_page.py
# @Software: PyCharm
# @desc    :
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage
from myappium.qiyeweixin.framework_basepage.pages.contact.personal_info_page import PersonalInfoPage


class SearchPage(BasePage):
    """
    检索页面
    """
    search_element = (MobileBy.ID, 'com.tencent.wework:id/fxc')

    def send_search_key(self,name) -> list:
        """
        输入要检索的值，返回查询到的结果列表
        :param name: 要检索的姓名
        :return:     查询到的结果列表
        """
        #先清空
        self.clear_input(self.search_element)
        # 输入搜索值
        self.find_and_sendkeys(self.search_element, name)
        sleep(2)
        # 校验搜索结果
        search_element_list = self.find_elements_by_text(name)

        return search_element_list


    def goto_personal_info_page(self,searchlist):
        """
        检查检索结果,数据量>1,则进行后续删除动作，否则止于此步
        :return:
        """
        # 如果检索到有值，则进入个人信息页面进行下一步操作
        if len(searchlist) <= 1:
            print('没有找到要删除的数据')
            return
        searchlist[-1].click()

        return PersonalInfoPage(self.driver)


    def assert_search_result(self,a,b):
        """
        断言检索结果
        :return:
        """
        assert a - b == 1







