from lxml import etree
import requests

def qs_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    titles = html.xpath("//div[@class='cont']/p[1]/a/b/text()")

    times =  html.xpath("//p[@class='source']/a[1]/text()")
    
    authurs = html.xpath("//p[@class='source']/a[2]/text()")
    
    contents = html.xpath("//div[@class='contson']/p/text()")

    #contents = html.xpath("//div[@class='contson']/br[1]/text()")

    #contents2 = html.xpath("//div[@class='contson']/br/text()")

    #contents3 = html.xpath("//div[@class='contson']/br/br/text()")

    #contents.xpath('string(.)')

    #c1 = contents[0].xpath('string(.)').strip()
    


    #pages = html.xpath()

    for title,time,authur,content in zip(titles,times,authurs,contents):
        print(f"{title} 朝代：{time} 作者：{authur} ")
        print(f"{content}")
        print("--------------------------------------------")

if __name__ == "__main__":

    urls = [f'https://www.gushiwen.org/default_{i}.aspx' for i in range(0,9,1)]

    for url in urls:
        qs_list(url)