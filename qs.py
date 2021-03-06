import requests
import re

def pa_list(url):

    resq = requests.get(url)

    html = resq.text

    names = re.findall('<h2>(.*?)</h2>',html,re.S)

    contents = re.findall('<span>.\n(.*?)</span>',html,re.S)

    fms = re.findall('div class="articleGender(.*?)Icon"',html,re.S)

    ages = re.findall('div class="articleGender.*?Icon">(.*?)</div',html,re.S)

    laughs = re.findall('<i class="number">(.*?)</i>',html,re.S)

    for name, content, fm, age, laugh in zip(names, contents, fms, ages, laughs):

        print(f"{name}{content.replace('<br/>','')}{fm}{laugh}")
if __name__ == "main__":

     urls = [f'https://www.qiushibaike.com/text/page/{i}/' for i in range(1,10,1)]

     for url in urls:
          pa_list(url)