import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class TestRemote():
    def setup(self):

        # 和浏览器打开的调试端口进行通信
        # 浏览器要使用 --remote-debugging-port=9222 开启调试，
        # 由于我环境变量设置了变量，alias driver_debugging='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222'
        # 所以可以直接：driver_debugging
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)

        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_remote_debug(self):
        self.driver.get('https://work.weixin.qq.com/')
        print(self.driver.get_cookies())

        #需要先把cookie通过上面输出拿到！！！
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850531850742'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'vgscVE3VGgiPjV30XldyHi3EUQKjNodt_6_Qwbw4nWzUofU_oEx6SZkhlAgH7quP62WK-jjMZQNtYqziVOB1RdcQOabcDuPTVUr0S6gHHUnutUJzcwopYSDkNgfpvKO0opQ9eaUMZ2iObEzf3aJ0eV6a9CAuY8HDVydNN9ul4d8jubW9QjPEiQnjpWpweubgTFqMrnY_XMsjgliOQIPkTorHZd9LAHR6Y3ZRKCfyWcFrV-efbS3Ee7lKlALiS3IoSrBO1gWDJDYFJPoHVoomxg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850531850742'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325138147142'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635123071, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603423179,1603424356,1603432114,1603587072'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a465902'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'lvWc6ImOzsx44Nw-2SegyPPHX8uqWusdX1--FRtZmlTwGtXpJJDZs1thbnrnJ1a6'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603587072'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '27653759673052281'}, {'domain': 'work.weixin.qq.com', 'expiry': 1603618588, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4fl4ave'}, {'domain': '.qq.com', 'expiry': 1603673463, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1367439684.1603424001'}, {'domain': '.work.weixin.qq.com', 'expiry': 1606179071, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1603587113, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1635123052, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1666659063, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1583622381.1594901080'}]

        # # 创建或者打开一个数据库
        db = shelve.open("cookies")
        # # 将数据存储到 shelve 中
        db["cookies"] = cookies
        #
        # # 取出数据
        cookies = db["cookies"]

        # 把cookie 中的时间戳去除"expiry",然后加入到浏览器的cookies中
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            # 把字典加入到 driver 的 cookie 中
            self.driver.add_cookie(cookie)

        sleep(2)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        sleep(2)
        self.driver.find_element(By.ID,'menu_contacts').click()
        sleep(2)
        db.close()




