# -*- coding: utf-8 -*-
import allure
import pytest
from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.support.wait import WebDriverWait


# 浏览器预置fix,默认scope为function，每个用例都会跑一次
@pytest.fixture()
def browser():
    # 01 用例前置操作
    # 初始化浏览器
    # 定义全局变量driver，本文件其他fix也能直接用
    global driver
    driver = webdriver.Chrome()

    # 移动窗口
    driver.set_window_position(1900, -200)
    driver.set_window_size(1550, 1000)

    # 02 用例执行，返回driver,username,password,wait
    yield driver

    # 03 用例后置，关闭浏览器
    driver.quit()