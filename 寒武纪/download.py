import os
import requests
url = "https://192.168.215.44:17810"
sid = "user1"
re = requests.get(url=url)

qes = re.text
print(qes)