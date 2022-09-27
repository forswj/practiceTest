import random
import os
import sys
import pysnooper
import csv

@pysnooper.snoop()
def createPhone():
    """生成随机手机号"""
    # choice方法随机抽取列表中的手机号码段
    str_start = random.choice(['135', '136', '138', "186"])
    # sample方法，列表中随机抽取8个尾数
    str_end = ''.join(random.sample('0123456789', 8))
    phone = str_start + str_end
    # 返回的手机号
    return phone

# def donum(num):
#     count = 0
#     while count <= num:
#         #print(createPhone())
#         count += 1

@pysnooper.snoop()
def writeNum(no):
    count = 1
    fpath = "..\\data\\mobile.csv"
    while count <= no:
        count += 1
        with open(fpath, 'a', encoding='utf-8') as cfile:
            cfile.write(createPhone()+'\n')
            #filednames = ['Mobile']
            #writer = csv.writer(cfile)
            #writer.writeheader()
            # try:
            #     writer.writerow({'手机号码': createPhone()})
            # except UnicodeEncodeError:
            #     print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

if __name__ == "__main__":
    #phone = donum(11)
    phone = writeNum(1)
