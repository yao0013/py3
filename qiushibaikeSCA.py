import requests
import re


'''def  prash_list(url)

     proxies = {
      #"http":"http://ip:端口号"
      "https":"https://113.128.29.232:9999"
     }'''

     url = http://www.qiushibaike.com/text
     
     resq = requests.get(url=url，proxies=https://120.83.104.108:9999)

     html = resq.text

     names = re.findall('<h2>(.*?)</h2>',html,re.S)

     contents = re.findall('<span>.\n(.*?)</span>',html,re.S)

     fms = re.findall('div class="articleGender(.*?)Icon"',html,re.S)

     ages = re.findall('div class="articleGender.*?Icon">(.*?)</div',html,re.S)

     laughs = re.findall('<i class="number">(.*?)</i>',html,re.S)


for name in names:
     print(name.strip())

for content in contents:
    print(content.replace('<br/>',''))

for fm in fms:
    print(fm)

for age in ages:
     print(age)

for laugh in laughs:
     print(laugh)

#for name, content, fm, age, laugh in zip(names, contents, fms, ages, laughs):
    print(f" {name} , {actor.strip()} , {time} , 评分：{c}{n} ")


#if __name__ =="main__":

#     url = [f'']