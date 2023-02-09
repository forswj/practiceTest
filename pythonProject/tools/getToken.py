import requests, json
from params_VAR import kanjia


class Token():
    def __init__(self):
        self.codeRsUrl = "https://account.saas.weimobqa.com/v2/api/console/getCodeRs"
        self.loginUrl = "https://account.saas.weimobqa.com/v2/api/console/login"
        self.header = {
            "content-type": "application/json; charset=utf-8",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        self.username = kanjia.USERNAME
        self.password = kanjia.PASSWORD


    def get_token(self):
        '''
        获取token
        :return:
        '''
        # r = requests.session()
        # 准备codeRsUrl接口入参
        param = {
            "zone": "0086",
            "phoneNumber": self.username,
            "pageName": "login"
        }
        cookie = requests.post(url=self.codeRsUrl, headers=self.header, json=param).cookies
        # 准备loginUrl接口入参
        param1 = {
            "zone": "0086",
            "phone": self.username,
            "password": self.password,
            "passwordType": "new",
            "remember": False,
            "ticket": None,
            "randstr": None
        }
        res = requests.post(url=self.loginUrl, json=param1, headers=self.header, cookies=cookie).json()
        token = res.headers.get('set-cookie')

        return 'Bearer' + ' ' + token


if __name__ == '__main__':
    tk = Token().get_token()
    print(tk)