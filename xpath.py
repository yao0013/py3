from lxml import etree
import requests

def qs_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    titles = html.xpath("//div[@class='cont']/p[1]/a/b")

    Times =  html.xpath("//p[@class='source']/a[1]")
    
    authurs = html.xpath("//p[@class='source']/a[2]")
    
    contents = html.xpath("//div[@class='cont']/div[@id]")

