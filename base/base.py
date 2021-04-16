"""
公共方法抽取
调用日志方法
"""

from datetime import datetime
from time import localtime, time, strftime
import allure
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_log import GetLog

log = GetLog.get_logger()


# 获取图片路径并通过动态时间+err.png组合方式拼接
filename = './image' + '/' + strftime("%Y-%m-%d-%H-%M-%S", localtime(time())) + '-' + '异常截图.png'

class Base:

    # 初始化方法
    def __init__(self, driver):
        log.info("正在初始化driver:{}".format(driver))
        """解决driver"""
        self.driver = driver

        # 获取查找方法封装
        # def base_find(self, loc, timeout=30, poll=0.5):
        """
        显示等待：
            （1）可以查找元素
            （2）可以修改元素查找的频率
        传递两个参数的方式：列表或元组  loc[0],loc[1] *loc
            loc为列表或元组
            *loc为解包==loc[0],loc[1]
            匿名函数参数x表示driver
        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout:查找元素超时时间，默认30秒
        :param poll:查找元素频率，默认0.5s
        :return:返回元素
        """
        # return WebDriverWait(self.driver,
        #                      timeout=timeout,
        #                      poll_frequency=poll).until(lambda x: x.find_element(*loc))

    def base_find(self, loc):
        log.info("正在查找元素:{}".format(loc))
        return WebDriverWait(self.driver, 15).until(lambda x: x.find_element(*loc))

    # 输入方法封装
    def base_input(self, loc, text):
        """
        :param loc: 元素定位信息
        :param text: 要输入的
        """
        # 1.获取元素
        el = self.base_find(loc)
        # 2.清空操作
        log.info("正在对:{}元素执行清空操作！".format(loc))
        el.clear()
        # 3.输入操作
        log.info("正在对:{}元素执行输入：{}操作！".format(loc, text))
        el.send_keys(text)

    # 点击方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        log.info("正在对:{}元素执行点击操作！".format(loc))
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 返回元素的文本值
        """
        log.info("正在对:{}元素获取文本操作！,获取的文本值:{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 获取弹框文本信息
    def base_get_alertText(self):
        alert = self.driver.switch_to.alert
        log.info("正在获取弹框文本信息：{}".format(alert.text))
        return alert.text

    # 获取文档标题
    def base_get_title(self):
        log.info("正在获取文档标题：{}".format(self.driver.title))
        return self.driver.title

    # 截图方法1
    def base_get_img(self):
        log.error("断言出错,正在执行截图操作！")
        # 1.截图保存图片路径
        self.driver.get_screenshot_as_file(filename)
        # 2.调用图片写入报告方法
        log.error("正在将错误图片写入报告！")
        self.__base_write_img()

    # 将图片写入报告方法（私有方法）
    def __base_write_img(self):
        with open(filename, mode='rb') as f:
            file = f.read()
        # 调用allure报告附加描述方法
        allure.attach(file, '附件截图', allure.attachment_type.PNG)

    # 截图方法2
    def base_save_screenshot(self, img_doc):
        log.error("断言出错,正在执行截图操作！")
        """
        页面截屏保存截图
        :param img_doc: 截图说明
        :return:
        """
        file_name = './image' + "\\{}_{}.png".format(datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S"), img_doc)
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, img_doc, allure.attachment_type.PNG)
