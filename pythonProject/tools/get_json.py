#导入json包
import json
import pymysql

# 打开json文件获取文件流
# with open("../data/login.json", "r", encoding="utf-8") as f:
#     # 调用load方法加载文件流
#     data = json.load(f)
#     print("获取的数据为：" , data)

# 使用函数进行封装
# def read_json():
#     with open("../data/login.json", "r", encoding="utf-8") as f:
#         # 调用load方法加载文件流
#         return json.load(f)

# 当需要使用多个json文件去获取参数时，使用参数来替代静态文件名
class GetJson(object):
    #初始化参数
    def __init__(self, filename):
        self.filepath = "../data/" + filename

    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)

if __name__ == '__main__':
    GetJson("login.json").read_json()