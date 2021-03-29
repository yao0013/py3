import requests
import re

url = "http://www.maoyan.com/board/7"

resq = requests.get(url=url)

html = resq.text

names = re.findall('<p class="name"><a.*?title="(.*?)"',html,re.S)

actors = re.findall('<p class="star">(.*?)</p>',html,re.S)

times = re.findall('<p class="releasetime">(.*?)</p>',html,re.S)

fen1 = re.findall('<p class="score"><i class="integer">(\d\.)',html,re.S)

fen2 = re.findall('</i><i class="fraction">(\d)</i>',html,re.S)


'''for name in names:
    print(name)

for actor in actors:
    print(actor.strip())

for time in times:
    print(time)

for c, n in zip(fen1, fen2):
    print(f"评分： {c}{n}")'''

for name, actor, time, c, n in zip(names, actors, times, fen1, fen2):
    print(f" {name} , {actor.strip()} , {time} , 评分：{c}{n} ")
