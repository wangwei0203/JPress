from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
import page
from selenium.webdriver.support import expected_conditions as EC
from tool.get_log import GetLog

log = GetLog.get_logger()

class LoginPage(Base):
    # 输入账号
    def page_input_user(self, user):
        # 调用父类输入方法
        self.base_input(page.user, user)

    # 输入密码
    def page_input_pwd(self, pwd):
        # 调用父类输入方法
        self.base_input(page.pwd, pwd)

    # 输入验证码
    # 调用父类输入方法
    def page_input_verify(self, captcha):
        self.base_input(page.captcha, captcha)

    # 点击登录按钮
    def page_click_login_btn(self):
        sleep(2)
        # 调用父类点击方法
        self.base_click(page.longinBtn)

        # 判断alert弹出框
        # result = EC.alert_is_present()(self.driver)
        # if result:
        #     print(result.text)
        #     result.accept()
        # else:
        #     print("alert未弹出")

    def page_alertText(self):
        # 等待提示框
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        return self.base_get_alertText()

    def page_alert(self):
        # 等待提示框
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        self.driver.switch_to.alert.accept()

    # 获取cookies
    def page_get_cookies(self):
        for cookies in self.driver.get_cookies():
            print(cookies)

    def page_add_cookie(self):
        self.driver.add_cookie({"name": "_jfinal_captcha",
                                "value": "9465b06f604f43cbb30d4d3a73f2b0ea"})
        self.driver.add_cookie({"name": "_jpanonym",
                                "value": "ZTdiMjMwM2E1ZmQwNmNiMDAxZmNjNTM2ODU3MGY3MjIjMTYxODkzNTQyNzMzMCMzMTUzNjAwMCNOV0ZtWmpoak9HWXhabVUyTkRjek5qZ3hOamhoTmpCbVpqazVaVEUyT1dFPQ=="})
        self.driver.add_cookie({"name": "Hm_lpvt_bfe2407e37bbaa8dc195c5db42daf96a", "value": "1618994438"})
        self.driver.add_cookie({"name": "Hm_lvt_bfe2407e37bbaa8dc195c5db42daf96a", "value": "1618994438"})
        self.driver.add_cookie({"name": "_jpuid",
                                "value": "MWFmNWE5NDgzMzM4ZjU1YjYwNWQzNjk2MDZkNThkODQjMTYxODk5NDQzNjE5MyMxNzI4MDAjTVE9PQ=="})
        self.driver.add_cookie({"name": "csrf_token", "value": "3d3f3c7eb5da4c9cbf61af4ae4a8dfd8"})
        
        sleep(3)
        self.driver.get("http://localhost:8088/jpress/admin/index")

    def page_get_title(self):
        return self.base_get_title()


    # 组合业务方法  --> 测试脚本业务层调用
    """调用相同页面操作步骤，跨页面不考虑"""

    def page_login(self, user, pwd, captcha):
        log.info("正在调用JPress后台登录业务方法,用户名:{},密码:{},验证码:{}".format(user, pwd, captcha))
        self.page_input_user(user)
        self.page_input_pwd(pwd)
        self.page_input_verify(captcha)
        self.page_click_login_btn()
