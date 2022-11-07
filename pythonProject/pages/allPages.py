#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 页面元素定位文件

"""
登录页
https://account.saas.weimobqa.com/login.html
page_login
"""
# 用户名  //*[@id="loginForm_phone"]
# page_login_user = ['id', 'loginForm_phone']
page_login_user = ['xpath', '//*[@id="loginForm_phone"]']
# 密码
# page_login_Pwd = ['id', 'loginForm_password']
page_login_Pwd = ['xpath', '//*[@id="loginForm_password"]']
# 登陆按钮 //*[@id="loginForm"]/div[6]/div[1]/div/div/div/div/button
page_login_loginBtn = ['xpath', '//*[@id="loginForm"]/div[6]/div[1]/div/div/div/div/button']