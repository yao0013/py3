import requests
import re

url = "http://www.maoyan.com/board/6"

resq = requests.get(url=url)

html = resq.text

names = re.findall('<p class="name"><a.*?title="(.*?)"',html,re.S)

actors = re.findall('<p class="star">(.*?)</p>',html,re.S)

times = re.findall('<p class="releasetime">(.*?)</p>',html,re.S)


for name, actor, time, in zip(names, actors, times,):
    print(f" {name} , {actor.strip()} , {time}  ")
