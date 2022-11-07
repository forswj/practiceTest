from time import time

from pages.allPages import page_login_user, page_login_Pwd, page_login_loginBtn
from params_VAR.kanjia import USERNAME, PASSWORD
from tools.webkeys import open_brower, WebKeys


# 打开浏览器对象
browers = WebKeys("Chrome")
# 输入地址
browers.open("http://master.saas.weimobqa.com/bos/products/mkBargain/4000255094976/5ybh1451gX2ryvojX5ydniao86/bargain/activity")
# 切换密码登录
browers.click('xpath', '//*[@id="loginForm_loginType"]/span[3]')
print(page_login_user)
browers.input(page_login_user[0], page_login_user[1], USERNAME)
browers.input(page_login_Pwd[0], page_login_Pwd[1], PASSWORD)
browers.click(page_login_loginBtn[0], page_login_loginBtn[1])
browers.wait(10)
browers.quit()