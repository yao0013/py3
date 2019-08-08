import requests
from lxml import etree

def get_url(url):

    html1 = requests.get(url).text
    html = etree.HTML(html1)
    #wallpaper_name = html.xpath(
    #    '//ul/li/figure/a/@title')
    wallpaper_urls = html.xpath('//ul/li/figure/a/@href')
    #print(wallpaper_url)
    return (wallpaper_urls)

def get_down(wallpaper_urls):

    for wurl in wallpaper_urls:

        html2 = requests.get(url=wurl).text

        html3 = etree.HTML(html2)

        download = html3.xpath('//section/div/img/@src')
        
        resp = requests.get (download)
        if not os.path.exists('./pics'):
            os.makedirs('./pics')
 
        with open('./pics/download','wb') as fp:
            fp.write(resp.content)


def main():
    urls = [f'https://wallhaven.cc/toplist?page={i}' for i in range(1,3)]
    for url in urls:
        wallpaper_urls = get_url(url)
        get_down(wallpaper_urls)

if __name__ == '__main__':
    main()