#!/usr/bin/env python
#!encoding:utf-8
import requests, re
from lxml import etree
import csv

def douban_list(url):
    data = requests.get(url).text
    data = etree.HTML(data)
    file = data.xpath('//*[@id="content"]/div/div[1]/div/table')
    item_list = []
    for html in file:
        info = [
            #'书名'
            html.xpath('.//tr/td[2]/div[1]/a/text()')[0].replace ('\n', '').replace (' ', '') if len(html.xpath ('.//tr/td[2]/div[1]/a/text()')) > 0 else '空',
            #'信息'
            html.xpath('.//tr/td[2]/p[1]/text()')[0].replace ('\n', '').replace (' ', '') if len(html.xpath ('.//tr/td[2]/p[1]/text()')) > 0 else '空',
            #'评分'
            html.xpath ('.//tr/td[2]/div[2]/span[2]/text()')[0].replace ('\n', '').replace (' ','') if len(html.xpath ('.//tr/td[2]/div[2]/span[2]/text()')) > 0 else '空',
            #'评价数'
            html.xpath ('.//tr/td[2]/div[2]/span[3]/text()')[0].replace ('\n', '').replace (' ','').strip("(").strip().strip(")").strip() if len(html.xpath ('.//tr/td[2]/div[2]/span[3]/text()')) > 0 else '空',
            #'金句'
            html.xpath('.//tr/td[2]/p[2]/span/text()')[0].replace ('\n', '').replace (' ', '') if len (html.xpath ('.//tr/td[2]/p[2]/span/text()')) > 0 else '空'
        ]
        item_list.append(info)
    return(item_list)

def write_list(info_list):
    for info in info_list:
        with open ('douban_list.csv', 'a+', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(info)

if __name__ == "__main__":
    with open ('douban_list.csv', 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        headers = ['书名','信息','评分','评价数','金句']
        writer.writerow(headers)
    
    urls = [ f'https://book.douban.com/top250?start={i}' for i in range(0, 225, 25) ]
    for url in urls:
        info_list = douban_list(url)
        write_list(info_list)
