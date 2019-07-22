import requests
import re

url = "https://www.qiushibaike.com/text/"

resq = requests.get(url=url)

html = resq.text

names = re.findall('<h2>(.*?)</h2>',html,re.S)

contents = re.findall('<span>.\n(.*?)</span>',html,re.S)


fms = re.findall('div class="articleGender(.*?)Icon"',html,re.S)

ages = re.findall('div class="articleGender.*?Icon">(.*?)</div',html,re.S)

laughs = re.findall('<span class="stats-vote"><i class="number">(.*?)</i> 好笑',html,re.S)

'''for name in names:
    print(name.strip())

for content in contents:
    print(content.replace('<br/>',''))

for fm in fms:
    print(fm)

for age in ages:
     print(age)

for laugh in laughs:
     print(laugh)'''

for name, content, laugh in zip(names, contents, laughs):
    print(f"作者:{name.strip()}  好笑数：{laugh.strip()} {content.replace('<br/>','') }  ")
