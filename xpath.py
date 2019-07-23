from lxml import etree
import requests

def qs_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    titles = html.xpath("//div[@class='cont']/p[1]/a/b")

    times =  html.xpath("//p[@class='source']/a[1]")
    
    authurs = html.xpath("//p[@class='source']/a[2]")
    
    contents = html.xpath("//div[@class='cont']/div[@id]")

    for title,time,authur,content in zip(titles,times,authurs,contents):
        print(f"{title}{time}{authur}{content}")

if __name__ == "__main__":

    urls = [f'https://www.gushiwen.org/default_{i}.aspx' for i in range(0,9,1)]

    for url in urls:
        qs_list(url)