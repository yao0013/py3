import requests
from lxml import etree
import re
url = 'http://192.168.203.38/portal/#/login'
resq = requests.get(url=url)
print(resq)
h1 = resq.text
print(h1)
html = etree.HTML(resq.text)
print(html)
titles = html.xpath("/html/body/div[@id='app']/div[@class='container']/div[@class='login-panel']/div[@class='login_form']/div[@class='loginButton']/button")
print(titles)