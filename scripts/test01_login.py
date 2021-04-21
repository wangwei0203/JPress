"""
本小节总结：
    一.重点
    （1）初始化方法和销毁（结束）方法选择：
       a.如果有多条参数化数据，采用类方法
       b.如果没有参数化数据，使用类方法或函数方法没有区别
    （2）调用业务层page方法
       a.通过统一入口类（PageIn）来实践
    （3）测试业务层常用方法：
        a.初始化
        b.结束（销毁）
        c.测试业务方法

"""

from time import sleep
import pytest
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
import unittest
from ddt import ddt, data, unpack, file_data
from tool.get_log import GetLog
from tool.read_userYaml import read_yaml

log = GetLog.get_logger()
excepted = None
title = None


@ddt
class TestLogin(unittest.TestCase):

    # 初始化
    def setUp(self) -> None:
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_login)

        # 2.通过统一入口类获取LoginPage对象
        self.login = PageIn(driver).page_get_LoginPage()

    # 结束
    def tearDown(self) -> None:
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    # 参数化
    # @pytest.mark.parametrize("user,pwd,captcha", read_yaml('user.yaml'))
    @data(('wangwei', '123456', ''), ('汪为', '', '8888'))
    @unpack
    # @file_data('../data/user.yaml')
    def test_login1(self, user, pwd, captcha):
        # 调用登录业务方法---> 密码为空
        self.login.page_login(user, pwd, captcha)
        self.excepted = '密码不能为空'
        actual = self.login.page_alertText()
        sleep(1)
        self.login.page_alert()
        try:
            # 断言
            assert self.excepted == actual
        except Exception as e:
            log.error("断言出错,错误信息:{}".format(e))
            print("错误原因", e)
            # 截图
            self.login.base_save_screenshot(img_doc='登录页面截图')
            # 抛出异常
            raise

    def test_login2(self, user='admin', pwd='123456', captcha='666'):
        # 调用登录业务方法---> 验证码不正确
        self.login.page_login(user, pwd, captcha)
        self.excepted = '验证码不正确'
        actual = self.login.page_alertText()
        sleep(1)
        self.login.page_alert()
        try:
            # 断言
            assert self.excepted == actual
        except Exception as e:
            log.error("断言出错,错误信息:{}".format(e))
            print("错误原因", e)
            # 截图
            self.login.base_save_screenshot(img_doc='登录页面截图')
            # 抛出异常
            raise

    def test_login3(self, user='', pwd='123456', captcha='666'):
        # 调用登录业务方法 --->账号为空
        self.login.page_login(user, pwd, captcha)
        self.excepted = '账号能为空'
        actual = self.login.page_alertText()
        sleep(1)
        self.login.page_alert()
        try:
            # 断言
            assert self.excepted == actual
        except Exception as e:
            log.error("断言出错,错误信息:{}".format(e))
            print("错误原因", e)
            # 截图
            self.login.base_save_screenshot(img_doc='登录页面截图')
            # 抛出异常
            raise

    # 获取cookies实现免登录
    def test_login4(self):
        # 通过获取cookie并添加cookie实现免登录
        self.login.page_get_cookies()
        sleep(3)
        self.login.page_add_cookie()
        sleep(6)
        self.title = 'JSpress后台登录'
        # 断言
        try:
            assert self.title == self.login.page_get_title()
        except Exception as e:
            # log.error("断言出错,错误信息:{}".format(e))
            print("错误原因", e)
            sleep(5)
            # 截图
            self.login.base_save_screenshot(img_doc='登录页面截图')
            # 抛出异常
            raise


# if __name__ == '__main__':
#     pytest.main()
