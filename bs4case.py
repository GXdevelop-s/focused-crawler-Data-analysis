# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月27日
"""
# 需求： 使用bs4爬取https://www.shicimingju.com/book/sanguoyanyi.html网站下三国演绎整本书（包括目录和内容）
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    head = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }
    page_text = requests.get(url=url, headers=head).text.encode('ISO8859-1')    # 不是utf-8编码了
    page_soup = BeautifulSoup(page_text, 'lxml')
    # 获取所有a标签
    a_list = page_soup.select('.book-mulu a')
    # 持久化存储
    with open(r'../gotpages/sanguo.txt', 'w', encoding='utf-8') as stream:
        for a in a_list:
            # 章节目录获取
            title = a.text
            detail_url = 'https://m.shicimingju.com' + a['href']
            # 详情页爬取
            detail_text = requests.get(url=detail_url, headers=head).text.encode('ISO8859-1')
            detail_soup = BeautifulSoup(detail_text, 'lxml')
            # 这里不能用select，因为select返回的是列表，列表中各个元素才能直接.text
            chapter_text = detail_soup.find('div', class_='chapter_content').text
            stream.write(title + ':\n' + chapter_text + '\n')
            print(title, '  爬取成功')
    print('over')
