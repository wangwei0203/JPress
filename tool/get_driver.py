"""
本小节总结：
  一.重点：
    1.获取driver和退出driver方法使用类方法（方便使用--不用示例化）
    2.driver为类属性，设置之前必须进行判断是否为空（目的：保存多次调用获取方法，返回同一个对象）
    3.返回driver语句和if判断为统一层级
    4.关闭driver必须置空操作
      a.driver执行quit方法后对象地址保留，不为空
      b.避免下条用例调用获取driver能正常获取对象，必须置空
"""

from selenium import webdriver
class GetDriver:
    # 1.声明变量
    _web_driver = None

    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('useAutomationExtension', False)
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 判断是否为空
        if cls._web_driver is None:
            # 设置driver操作
            # 1.获取浏览器
            cls._web_driver = webdriver.Chrome(options=option)
            # 2.最大化浏览器
            cls._web_driver.maximize_window()
            # 3.打开url
            cls._web_driver.get(url)
        # 返回driver
        return cls._web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls._web_driver:
            # 退出操作
            cls._web_driver.quit()
            # 置空操作(重点)
            cls._web_driver = None
