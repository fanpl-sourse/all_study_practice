# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 15:27
# @Author  : 饭盆里
# @File    : register_po.py
# @Software: PyCharm
# @desc    :
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegistorPo:
    """
    注册企业微信页面
    """
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def registor(self,corp_name,manager_name,register_tel):
        """
        注册企业微信
        :return:
        """
        self.driver.find_element(By.ID,'corp_name').send_keys(corp_name)
        #下拉框定位
        self.driver.find_element(By.CSS_SELECTOR,'.js_corp_industry_btn').click()
        self.driver.find_element(By.CSS_SELECTOR,'.register_industry_maintype_item_link').click()
        self.driver.find_element(By.XPATH,'//*[@id="corp_industry"]/div/table/tbody/tr/td[2]/div[1]/div[1]/a').click()

        self.driver.find_element(By.XPATH,'//*[@id="corp_scale_btn"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="corp_scale_btn"]/div/ul/li[1]/a/span[2]').click()

        self.driver.find_element(By.ID,'manager_name').send_keys(manager_name)
        self.driver.find_element(By.ID,'register_tel').send_keys(register_tel)
        self.driver.find_element(By.ID,'iagree').click()

        self.driver.find_element(By.ID,'submit_btn').click()






