import requests
import re

url = "https://www.qiushibaike.com/text/"

resq = requests.get(url=url)

html = resq.text

names = re.findall('<h2>(.*?)</h2>',html,re.S)

contents = re.findall('<span>.\n(.*?)</span>',html,re.S)

fms = re.findall('div class="articleGender(.*?)Icon"',html,re.S)

ages = re.findall('div class="articleGender.*?Icon">(.*?)</div',html,re.S)

laughs = re.findall('<i class="number">(.*?)</i>',html,re.S)


#for name in names:
 #   print(name.strip())

for content in contents:
    print(content.replace('<br/>',''))

for fm in fms:
    print(fm)

for age in ages:
     print(age)

for laugh in laughs:
     print(laugh)

     5