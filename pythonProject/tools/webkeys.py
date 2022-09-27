from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from tools.weboptions import options
from selenium import webdriver
import time

'''
    关键字驱动类：实现基于selenium的web自动化关键字驱动类，封装常用的web操作行为作为各种关键字
        1. 访问url
        2. 元素定位
        3. 输入
        4. 点击
        5. 悬停
        6. 滚动条
        7. iframe切换
        8. 句柄切换
        ......
    封装的函数考虑多样化的条件场景，以及高复用性
'''


# 创建driver对象
def open_brower(type_):
    browsers = {
        'Chrome': ['chrome', 'Chrome', 'CHROME', 'google chrome', '谷歌', '谷歌浏览器'],
        'Edge': ['edge', 'Edge', 'ed', '微软'],
        'Firefox': ['Firefox', 'FireFox', 'firefox', 'firefix', '火狐', '火狐浏览器']
    }

    try:
        if type_ in browsers['Chrome']:
            # 正常创建
            driver = webdriver.Chrome(options=options())
        elif type_ in browsers['Edge']:
            driver = webdriver.Edge(options=options())
        elif type_ in browsers['Firefox']:
            driver = webdriver.Firefox(options=options())
        else:
            # 基于反射机制实现driver对象
            driver = getattr(webdriver, type_)()
    except Exception as e:
        driver = webdriver.Chrome()
    return driver


# 封装操作关键字
class WebKeys:
    # 构造函数
    def __init__(self, type_):
        self.driver = open_brower(type_)
        self.driver.implicitly_wait(10)

    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 定位元素：一定是要满足各种定位方法，一定要添加return
    def locator(self, by, value):
        return self.driver.find_element(by, value)

    # 元素定位
    def locator(self,name,value):
        el = self.driver.find_element(name,value)
        # 将定位的元素框出来
        self.locator_station(el)
        return el

    # 显示定位的地方，方便确认定位位置
    def locator_station(self, element):
        self.driver.execute_script(
            "arguments[0].setAttribute('style',arguments[1]);",
            element,
            "border: 2px solid green;"  # 边框，green绿色
        )

    # 窗口切换
    def change_window(self, n):
        # 获取句柄
        handles = self.driver.window_handles
        # 切换到原始页面,n = 0
        # 切换句柄到第二个页面,n = 1 ,以此类推
        self.driver.switch_to.window(handles[n])
        print(self.driver.title)

    # 鼠标点击并悬停，用于处理鼠标点击会变化的动态元素
    def mouse_hold(self, url):
        btn = self.driver.find_elements(By.XPATH, url)[0]
        action = ActionChains(self.driver)
        action.click_and_hold(btn).perform()

    # 输入文本，并按回车键
    def send_enter(self, txt, name, url):
        self.locator(name, url).send_keys(txt + Keys.ENTER)

    # 输入
    def input(self, by, value, txt):
        # self.driver.find_element(by, value).send_keys(txt)
        self.locator(by, value).send_keys(txt)

    # 点击
    def click(self, by, value):
        self.locator(by, value).click()

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 强制等待
    def wait(self, time_):
        time.sleep(time_)

