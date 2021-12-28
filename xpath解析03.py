# -*- coding:utf-8 -*-
"""
作者: gaoxu
日期: 2021年12月28日
"""
# xpath解析原理     最常用且最便捷高效的一种解析方式，有通用性
'''
1.实例化一个etree的对象，且需要将被解析的页面源码数据加载
2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获
'''
from lxml import etree

# 实例化etree对象1
# etree.parse(filepath)
# 实例化etree对象2
# etree.HTML('page_text')
# -xpath('xpath表达式')    / 表示一个层级
if __name__ == '__main__':
    # 需要符合xml解析器的使用规范
    parser = etree.HTMLParser(encoding='utf-8')  # This parser allows reading HTML into a normal XML tree
    tree = etree.parse(r'F:\work\task1/3.html', parser=parser)

    # 标签定位
    r1 = tree.xpath('/html/head')  # 第一个/表示从根节点开始定位;
    print(r1)  # 返回值是一个列表，但不能直接看见标签，而是存放了标签元素在其中
    r2 = tree.xpath('/html//div')  # //表示多个层级
    print(r2)
    r3 = tree.xpath('//div')  # 可以从任意位置定位div
    print(r3)
    # 属性定位
    r4 = tree.xpath('//div/a[@href="#3"]')  # tag[@attrName="attrValue"]
    print(r4)
    # 索引定位
    r5 = tree.xpath('//div[@id="g"]/a[1]')
    print(r5)

    # 取文本
    # /text() 获取的是标签中直系的文本内容 返回一个字符串列表
    # //text()     获取的是标签中非直系（所有）的文本内容 返回一个字符串列表
    t5 = tree.xpath('//div[@id="g"]/a[1]/text()')
    print(t5)
    # 取属性
    # /@attrname
    attrvalue5= tree.xpath('//div[@id="g"]/a[1]/@href')
    print(attrvalue5)

