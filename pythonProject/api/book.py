#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lxml import etree


def book():
    url = "https://www.xbiquge.la/7/7194/"
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    url_list = html.xpath('//div[@id="list"]/dl/dd/a/@href')
    name_list = html.xpath('//div[@id="list"]/dl/dd/a/text()')
    fp = open("修真聊天群.txt", 'w')
    for ur, na in zip(url_list, name_list):
        res = requests.get(f'https://www.xbiquge.la{ur}')      # 向网站发送请求并获取网站数据
        res.encoding = 'utf-8'
        res_html = etree.HTML(res.text)
        info = res_html.xpath('//div[@id="content"]/text()')
        fp.write(f'{na}\n\n')
        print(f'{na}__{ur}')        # 查看当前章节名称和链接地址
        for i in info:
            i = i.replace(r'\xa0', '').replace('\n\n', '\n')        # 去除垃圾信息并调整排版
            if i == '\r':
                continue
            fp.write(i)         # 写入正文到文本中
        fp.write('\n\n')
    fp.close()


if __name__ == '__main__':
    book()