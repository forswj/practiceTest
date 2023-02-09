from params_VAR import kanjia
import requests

codeRsUrl = "https://account.saas.weimobqa.com/v2/api/console/getCodeRs"
loginUrl = "https://account.saas.weimobqa.com/v2/api/console/login"
username = kanjia.USERNAME
password = kanjia.PASSWORD


param = {
            "zone": "0086",
            "phoneNumber": username,
            "pageName": "login"
        }
header = {'Content-Type': 'application/json;charset=UTF-8'}
cookie = requests.post(url=codeRsUrl, headers=header, json=param).cookies
ck = requests.utils.dict_from_cookiejar(cookie)
#print(cookie)



header1 = {
        "content-type": "application/json; charset=utf-8",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Cookie":  str(ck),
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Origin": "http://account.saas.weimobqa.com",
        "weimob-country": "CN",
        "weimob-language": "zh"
    }

param1 = {
    "zone": "0086",
    "phone": username,
    "password": password,
    "passwordType": "new",
    #"remember": False,
}

res = requests.post(url=loginUrl, json=param1, headers=header1)
# print(res)
token = res.headers.get('Set-Cookie')
print(token)