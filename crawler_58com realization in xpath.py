# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月29日
"""
# 需求：爬取58同城中二手房的信息
from lxml import etree
import requests

if __name__ == '__main__':
    url = 'https://m.58.com/bj/ershoufang/?reform=pcfront'
    # UA伪装
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    # universal crawler
    page_text = requests.get(url=url, headers=head).text
    # xpath
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.HTML(page_text, parser=parser)
    print(tree)
    li_list = tree.xpath('//ul[@class="list"]/li[@class="item-wrap"]')
    print(li_list)
    with open(r'../gotpages/58secondhand_houses.txt', 'w', encoding='utf-8') as stream:
        for li in li_list:
            house_name = li.xpath('.//span[@class="content-title"]/text()')[0]
            #print(house_name)
            stream.write(house_name)
            print(house_name)

