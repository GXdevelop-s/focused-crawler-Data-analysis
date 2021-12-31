# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月31日
"""
# 需求：爬取彼岸图网的图片和图片名称并持久化存储
import os

import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://pic.netbian.com/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    response = requests.get(url=url, headers=head).text
    # response.encoding = 'utf-8'
    #parser = etree.HTMLParser(encoding='gbk')
    tree = etree.HTML(response)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')
    folder = '../gotpages/bianpics'
    print(li_list)
    for li in li_list:
        img_url = li.xpath('.//img/@src')[0]
        true_url = url + img_url
        img_name = li.xpath('.//img/@alt')[0]
        # 统用处理中文乱码的解决方案 也可以删除之后，把text改成content
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        save_path = folder + '/' + img_name + '.jpg'
        img_response = requests.get(url=true_url, headers=head).content
        if os.path.isdir(folder) is not True:
            os.mkdir(folder)
        with open(save_path, 'wb') as stream:
            stream.write(img_response)
            print(img_name, ': 下载成功')
