import requests
import re

url = "https://www.qiushibaike.com/text/"

def  prash_list(url):
     
     resq = requests.get(url=url)

     fms = re.findall('div class="articleGender(.*?)Icon"',html,re.S)

     ages = re.findall('div class="articleGender.*?Icon">(.*?)</div',html,re.S)

     laughs = re.findall('<i class="number">(.*?)</i>',html,re.S)

     fms = re.findall('div class="articleGender(.*?)Icon"',html,re.S)

     ages = re.findall('div class="articleGender.*?Icon">(.*?)</div',html,re.S)

     laughs = re.findall('<i class="number">(.*?)</i>',html,re.S)

     for name, content, laugh in zip(names, contents, laughs):
          print(f"作者:{name.strip()}  好笑数：{laugh.strip()} {content.replace('<br/>','') }  ")

#if __name__ =="main__":

     urls = [f'https://www.qiushibaike.com/text/page/{i}/' for i in range(1,10,1)]

     for url in urls:
          prash_list(url)
