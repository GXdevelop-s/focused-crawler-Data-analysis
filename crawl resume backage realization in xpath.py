# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2022年01月03日
"""
# 需求：从网站爬取模板的价格，原本的需求是批量下载网页上的模板，但是要付费
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://sc.chinaz.com/jianli/'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    page_text_resume = requests.get(url=url, headers=head).text
    tree = etree.HTML(page_text_resume)
    resume_page_url_list = tree.xpath('//div[@id="container"]/div/a/@href')
    # print(resume_page_url_list)
    resume_model_prices = []
    for resume_page_url in resume_page_url_list:
        resume_page_url = 'https:' + resume_page_url
        detail_text_resume = requests.get(url=resume_page_url, headers=head).text
        d_tree = etree.HTML(detail_text_resume)
        result = d_tree.xpath('//div[@class="pay-haed"]//span[2]/text()')
        resume_model_prices.extend(result)
    print(resume_model_prices)
