import requests
from lxml import etree

def get_url(url):
    url = "https://wallhaven.cc/toplist"
    html1 = requests.get(url).text
    html = etree.HTML(html1)
    #wallpaper_name = html.xpath(
    #    '//ul/li/figure/a/@title')
    wallpaper_url = html.xpath('//ul/li/figure/a/@href')
    #print(wallpaper_url)
    return (wallpaper_urls)

def get_magnet(wallpaper_urls):

    for wurl in wallpaper_urls:

        html2 = requests.get(url=wurl).text

        html3 = etree.HTML(html2)

        download = html3.xpath('//section/div/img/@src')
        


def main():
    urls = [f'http://www.mp4ba.com/dianying/list_{i}.html' for i in range(1,10)]
    for url in urls:
        movies = get_url(url)
        get_magnet(movies)

if __name__ == '__main__':
    main()'''