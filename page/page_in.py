"""
统一入口类编写
"""
from page.loginPage import LoginPage


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取LoginPage对象
    def page_get_LoginPage(self):
        return LoginPage(self.driver)
