# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 21:08
# @Author  : 饭盆里
# @File    : test_record_script.py
# @Software: PyCharm
# @desc    : 第一个录制的appium脚本

from appium import webdriver

desired_caps = {
    'platformName':'Android',
    'deviceName':'emulator-5554',
    'appPackage':'com.xueqiu.android',
    'appActivity':'.view.WelcomeActivityAlias'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("娃哈哈")
el4 = driver.find_element_by_id("com.xueqiu.android:id/name")
el4.click()
