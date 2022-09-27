from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains

'''
    浏览器配置类：专门用于配置chrome浏览器的默认启动设置。
        selenium2的版本中，浏览器的options是通过chrome_options参数进行传入
        selenium3开始，options都是基于options参数进行传入

        add_argument()函数用于添加浏览器的常规设定
        add_experimental_option()函数用于添加浏览器的实验性设定

        ChromeOptions指令大全，最全指令在chrome官方。可以自行搜索。

        自主设计可以满足所有浏览器的BrowserOptions：
            1. 基于不同浏览器封装不同的options方法，返回options对象
            2. 创建BrowserOptions，设置入参，基于入参的不同，调用不同的options方法，获得返回值，在函数中二次返回。
'''

def options():
    # 创建options对象
    options = webdriver.ChromeOptions()
    # 设置页面最大化
    options.add_argument('start-maximized')
    # 去掉控制台多余的信息
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

    return options


# 测试

# driver = webdriver.Chrome(options=options())
# driver.implicitly_wait(5)
# driver.get('http://www.baidu.com')
# sleep(3)
# driver.quit()
