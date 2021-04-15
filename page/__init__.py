"""以下为jpress登录url"""
# 登录url
url_login = "http://localhost:8088/jpress/admin/login"

"""
  以下数据为Jpress登录模块配置数据
"""
from selenium.webdriver.common.by import By
# 账号
user = (By.NAME, 'user')
# 密码
pwd = (By.NAME, 'pwd')
# 验证码
captcha = (By.NAME, 'captcha')
# 登录按钮
longinBtn = (By.CLASS_NAME, 'btn')



