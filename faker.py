import requests
from faker import Faker

f=Faker(locale='zh_CN')
'''def add_member():'''
headers = {

}
data = {

}

url = ''

for i in range(1500):
    resq = requests.post(url=url,data=data.headers=headers)