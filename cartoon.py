# -*- coding:utf-8 -*-
import requests, os, time
from lxml import etree

headers = { 
    'Cache-Control': 'max-age=86400',
    'Connection': 'keep-alive',
    'Date': 'Mon, 26 Aug 2019 14:24:28 GMT',
    'Expires': 'Tue, 27 Aug 2019 10:34:35 GMT',
    'Server':' openresty',
    'Vary': 'Accept-Encoding',
    'Via':' http/1.1 zats (zats4 [cRs f ])'
}

host = 'http://desk.zol.com.cn/'

def get_url(url):
    html1 = requests.get(url,headers=headers).text
    html = etree.HTML(html1)
    wallpa_urls = html.xpath('//ul/li/a[@class="pic"] /@href')
    wallpaper_urls=host + wallpa_urls
    return (wallpaper_urls)

def get_down(wallpaper_urls):
    for wurl in wallpaper_urls:
        html2 = requests.get(url=wurl,headers=headers).text
        html3 = etree.HTML(html2)
        download_url = html3.xpath('//section/div/img/@src')[0]
        pic_name = download_url.split('/')[-1]
        try:
            resp = requests.get (download_url,headers=headers)
        except Exception as e:
            print(str(e))
        time.sleep(3)
        with open('./pics/'+ pic_name,'wb') as fp:
            fp.write(resp.content)

def main():
    if not os.path.exists('./pics'):
        os.makedirs('./pics')
    urls = [f'http://desk.zol.com.cn/dongman/hot_{i}.html' for i in range(1,6)]
    for url in urls:
        wallpaper_urls = get_url(url)
        get_down(wallpaper_urls)

if __name__ == '__main__':
    main()
