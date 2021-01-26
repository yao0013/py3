import requests
from lxml import etree
import os
import time

def get_url(url):

    html1 = requests.get(url,headers={'Origin': 'https://wallhaven.cc','Referer': 'https://wallhaven.cc/w/q6lm7r','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}).text
    html = etree.HTML(html1)
    #wallpaper_name = html.xpath(
    #    '//ul/li/figure/a/@title')
    wallpaper_urls = html.xpath('//ul/li/figure/a/@href')
    #print(wallpaper_url)
    return (wallpaper_urls)

def get_down(wallpaper_urls):
    if not os.path.exists('./pics'):
        os.makedirs('./pics')

    for wurl in wallpaper_urls:
        html2 = requests.get(url=wurl,headers={'Origin': 'https://wallhaven.cc','Referer': 'https://wallhaven.cc/w/q6lm7r','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}).text
        html3 = etree.HTML(html2)
        download_url = html3.xpath('//section/div/img/@src')
        pic_name = download_url[0].split('\/')[-1]
        try:
            resp = requests.get (download_url,headers={'Origin': 'https://wallhaven.cc','Referer': 'https://wallhaven.cc/w/q6lm7r','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'})
        except Exception as e:
            print(str(e))
            time.sleep(3)    
        with open('./pics/'+ pic_name,'wb') as fp:
            fp.write(resp.content)

def main():
    urls = [f'https://wallhaven.cc/toplist?page={i}' for i in range(1,4)]
    for url in urls:
        wallpaper_urls = get_url(url)
        get_down(wallpaper_urls)

if __name__ == '__main__':
    main()