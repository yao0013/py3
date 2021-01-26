from lxml import etree
import requests
import csv

def douban_list(url):

    resq = requests.get(url = url)

    htmls = etree.HTML(resq.text)

    csv_list =[]
    headers = ['书名','信息','评分','评价数','金句']
    for html in htmls:

        info = {

            '书名' : html.xpath('.//tr/td[2]/div[1]/a/text()')[0].replace ('\n', '').replace (' ', '') if len (
                html.xpath ('.//tr/td[2]/div[1]/a/text()')) > 0 else '空',

            '信息' : html.xpath('.//tr/td[2]/p[1]/text()')[0].replace ('\n', '').replace (' ', '') if len (
                html.xpath ('.//tr/td[2]/p[1]/text()')) > 0 else '空',

            '评分' : html.xpath ('.//tr/td[2]/div[2]/span[2]/text()')[0].replace ('\n', '').replace (' ',
                                                                                                           '') if len (
                html.xpath ('.//tr/td[2]/div[2]/span[2]/text()')) > 0 else '空',

            '评价数' : html.xpath ('.//tr/td[2]/div[2]/span[3]/text()')[0].replace ('\n', '').replace (' ',
                                                                                                             '') if len (
                html.xpath ('.//tr/td[2]/div[2]/span[3]/text()')) > 0 else '空',

            '金句' : ('.//tr/td[2]/p[2]/span/text()')[0].replace ('\n', '').replace (' ', '') if len (
                html.xpath ('.//tr/td[2]/p[2]/span/text()')) > 0 else '空'

            #'ords' : html.xpath("//span[@class='inq']/text()")
        }
        csv_list.append(info)

    
        with open ('doubanmovie.csv', 'w', newline='', encoding='utf8') as f:
            writer = csv.DictWriter (f, headers)
            writer.writeheader ()
            writer.writerows (csv_list)

if __name__ == "__main__":

    urls = [f'https://book.douban.com/top250?start={i}' for i in range(0,225,25)]

    for url in urls:
        
        douban_list(url)