from lxml import etree
import requests

def qs_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    authurs = html.xpath()

    contents = 

    laughs = 

    click = 

