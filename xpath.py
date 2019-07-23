from lxml import etree
import requests

def qs_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    titles = html.xpath("/html/body/div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='cont']/p[1]/a/b")

    Times =  html.xpath("/html/body/div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='cont']/p[@class='source']/a[1]")
    
    authurs = html.xpath("/html/body/div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='cont']/p[@class='source']/a[2]")
    
    contents = html.xpath("/html/body/div[@class='main3']/div[@class='left']/div[@class='sons']/div[@class='cont']/div")

