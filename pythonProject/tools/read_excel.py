import json

import jsonpath
import openpyxl
# from openpyxl import load_workbook
import pandas


'''
    1、通过输入的数字找到表中对应的行
    2、获取对应行第二列到最后一列的参数
    3、格式化成json格式并输出
'''


# 输入数字
a = int(input('请输入应用对应第一列数字：'))

# 获取excel中的内容
#excel = openpyxl.load_workbook('../data/增购参数.xlsx')
df = pandas.read_excel('../data/增购参数.xlsx')

dataFile = []
for a in range(df.values):
    if a-1 > 0:
        dataFile.append(df.iloc[a-1].values)

print(dataFile)

# 定位到表单
#sheet = excel['Sheet1']
#

# for rows in sheet.rows:
#     print(list(rows))
#     if rows[0] != 0:
#         print(rows)

# for values in sheet.values:
#     # 获取增购参数表中的参数
#     if type(values[0]) is int:
#         print(a)
    # print(values[a-1])






