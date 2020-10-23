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
        # print(self.driver.get_cookies())
        #需要先把cookie通过上面输出拿到！！！
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '2GCIUzNPzJJgJoUMdzgt1XKA4wamBQAlIUG9yUJWh28xI0tlZtbAvkGnJxSMhxKtSbNg3kuKT23UGjevuAeTm582nUQBZ6y6_Ns1MCECl9X2htLsk2N-4-Ke65nI0IM9DYq_ixFBimyyp_ak8kqAPaLOd4cOFRCb4T7UCX02_ST4d6HJxl24UtJ92mij3bPxxozYbGq21PxVKuJY8zdHQ2xTnJ7OYzoUZVLHXAOqyr6yYWwffrxod5y4NzH6TKoTG1aeeevM0zwON46a-hXT2g'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a855756'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'lvWc6ImOzsx44Nw-2SegyEb_DJklcTVfKScNd41lK0KUr6JvDj2vPRLwumfvs1h4'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s3743457403'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850531850742'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850531850742'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325138147142'}, {'domain': 'work.weixin.qq.com', 'expiry': 1603454047, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '75vp3a0'}, {'domain': '.qq.com', 'expiry': 1603510918, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1367439684.1603424001'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '200bf20496381a574cfd663edcc91357102088c9788f83032c52f35af3563544'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634982707, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603422525,1603423179,1603424356,1603432114'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8752271993'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'Iow0CxrSRH'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603446707'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '26225621642883261'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '4034072576'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627635874, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1666496518, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1583622381.1594901080'}, {'domain': '.work.weixin.qq.com', 'expiry': 1606038706, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]

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



