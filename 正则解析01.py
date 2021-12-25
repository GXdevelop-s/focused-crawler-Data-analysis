# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月24日
"""
import os
import re

import requests
# 实现需求
if __name__ == '__main__':
    # UA伪装
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    url = 'https://www.qiushibaike.com/article/125034773'
    # 预备本地存放地址
    local_path = '../gotpages/image_folder'
    # 通用爬虫先爬取整个页面数据
    page_data = requests.get(url=url, headers=head).text
    # < img src = "//pic.qiushibaike.com/article/image/F6AHBXUBI3PQTTMT.jpg" alt = "糗事图片" >
    # 聚焦爬虫
    need_data1 = re.findall(r'<img src="(.*?)" alt="糗事图片">', page_data, re.M)
    for data in need_data1:
        # 合成实际地址
        url = 'https:' + data
        image_data = requests.get(url=url, headers=head).content

        if os.path.isdir(local_path) is False:
            os.mkdir(local_path)
        # 分离出图片名
        image_Part_Name = data.split('/')[-1]
        # 合成最终文件路径
        image_path = local_path + '/' + image_Part_Name
        with open(image_path,'wb') as stream:
            stream.write(image_data)
            print(image_Part_Name,'下载成功')
    print('over!')