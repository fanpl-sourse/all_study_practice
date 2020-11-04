# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 08:26
# @Author  : 饭盆里
# @File    : add_contact_page.py
# @Software: PyCharm
# @desc    :
from appium.webdriver.common.mobileby import MobileBy
from myappium.qiyeweixin.framework_basepage.basepage.basepage import BasePage

class AddContactPage(BasePage):
    """
    添加成员的操作页面
    """

    name_element = (MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@class="android.widget.EditText"]')
    gender_element = (MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]')
    male = (MobileBy.XPATH, f'//*[@resource-id="com.tencent.wework:id/dyx" and @text="男"]')
    female = (MobileBy.XPATH, f'//*[@resource-id="com.tencent.wework:id/dyx" and @text="女"]')
    mobilenum_element = (MobileBy.ID, 'com.tencent.wework:id/f1e')
    save_element = (MobileBy.XPATH, '//*[@text="保存"]')

    def send_name(self,name):
        """
        输入姓名
        :return:
        """
        # 输入【用户名】
        self.find(self.name_element).send_keys(name)
        return self

    def click_gender(self,gender):
        """
        点击选择性别
        :return:
        """
        # 性别
        self.find_and_click(self.gender_element)
        if gender == '男':
            self.find_and_click(self.male)
        else:
            self.find_and_click(self.female)

        return self

    def send_mobilenum(self,mobile):
        """
        输入手机号
        :return:
        """
        # 输入手机号
        self.find(self.mobilenum_element).send_keys(mobile)
        return self

    def click_save(self):
        """
        点击保存
        :return:
        """
        from myappium.qiyeweixin.framework_basepage.pages.contact.manual_add_contact_page import ManualAddContactPage
        # 保存
        self.find_and_click(self.save_element)
        return ManualAddContactPage(self.driver)

