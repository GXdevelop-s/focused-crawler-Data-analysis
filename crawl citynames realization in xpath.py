# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2022年01月02日
"""
# 需求：仅限使用一条xpath完成对热门/全部城市的名称爬取
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    page_text = requests.get(url=url, headers=head).text
    tree = etree.HTML(page_text)
    a_text_list = tree.xpath('//div[@class="hot"]//li/a/text() | //div[@class="all"]//div/li/a/text()')
    all_city_names = []
    for a_text in a_text_list:
        all_city_names.append(a_text)
    print(all_city_names)
    print(len(all_city_names))
