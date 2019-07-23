from lxml import etree
import requests

def qs_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    titles = html.xpath("//div[@class='cont']/p[1]/a/b/text()")

    times =  html.xpath("//p[@class='source']/a[1]/text()")
    
    authurs = html.xpath("//p[@class='source']/a[2]/text()")
    
    contents = html.xpath("//div[@class='cont']/div[@id]/text()")

    for title,time,authur,content in zip(titles,times,authurs,contents):
        print(f"{title} 朝代：{time} 作者：{authur} {content.strip()}")

if __name__ == "__main__":

    urls = [f'https://www.gushiwen.org/default_{i}.aspx' for i in range(0,9,1)]

    for url in urls:
        qs_list(url)