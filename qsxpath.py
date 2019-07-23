from lxml import etree
import requests

def qs_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    titles = html.xpath("//h2/text()")

    times =  html.xpath("//p[@class='source']/a[1]/text()")
    
    authurs = html.xpath("//p[@class='source']/a[2]/text()")
    
    contents = html.xpath("//div[@class='contson']/text()")

    #contents.xpath('string(.)')

    #c1 = contents[0].xpath('string(.)').strip()
    


    for title,time,authur,content in zip(titles,times,authurs,contents):
        print(f"{title} 朝代：{time} 作者：{authur} ")
        print(f"{content}")
        print("--------------------------------------------")

if __name__ == "__main__":

    urls = [f'https://www.qiushibaike.com/text/page/{i}/' for i in range(0,9,1)]

    for url in urls:
        qs_list(url)