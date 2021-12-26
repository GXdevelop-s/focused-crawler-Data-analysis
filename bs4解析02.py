# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月26日
"""
# bs4数据解析的原理
'''
    1.实例化一个beautifulSoup对象，并将页面源码数据加载到该对象中
    2.通过调用beautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
'''
# 环境安装
'''
pip install bs4
pip install lxml   (解析器)
'''
# 对象的实例化1(本地html文档加载到对象)
# with open(r'../gotpages/pdd.html','r',encoding='utf-8') as stream:
#     soup=BeautifulSoup(stream,'lxml')
# 对象的实例化2（网页上的源码数据加载到该对象）
# page_text=response.text
# soup=BeautifulSoup(page_text,'lxml')
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open(r'../gotpages/pdd.html', 'r', encoding='utf-8') as stream:
        soup = BeautifulSoup(stream, 'lxml')
        print(soup.a)  # soup.tagName 返回的是第一次出现的a标签
        print(soup.find('div'))  # find('tagName')等同于soup.tagName
        # 标签属性定位,注意要加下划线
        print(soup.find('div', class_='result-loading se-loading-pos se-loading'))
        # 找到所有符合要求的标签
        print(soup.find_all('a'))  # 返回值为列表

        # select
        # 参数是一种选择器，标签选择器，class选择器，id选择器等等,返回值是一个列表
        #  标签：tagName       类：.class        id： #id
        # print(soup.select('#page'))
        # 层级选择器
        print('*' * 10)
        print(soup.select('.se-form > div>div>i'))  # 类为se-form下的div下的div下的i标签（列表）
        print(soup.select('.se-form i'))  # >标识一个层级，空格表示多个层级

        # 获取标签之间的文本数据(两个属性一个方法)
        print(soup.select('.se-form i')[0].text)  # 可以获得某个标签中所有的文本内容
        print(soup.select('.se-form i')[0].get_text())
        print(soup.select('.se-form i')[0].string)  # 只可以获取该标签下面直系的文本内容

        # 获取标签中的属性值
        print(soup.a['class'])
