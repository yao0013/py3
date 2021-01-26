import requests
from faker import Faker

f=Faker(locale='zh_CN')
for i in range(1500):
    headers = {
    'Cookie': 'CID=e05ef3e6bcb4d7afa8accc77052726cf; SEID=4b315ba8e3f143a6e52d160100c35a3029b5ae48c9649e072dc1ca43407736826b58029e9fb18bf08b402648d830e7ac38902ae4070c82eabcc0a0ec; UID=110003619_N1_1569398339'
    }
    data = {
    'birthday':f.date(pattern="%Y-%m-%d"),
    'calendar':1,
    'naddress':'[{"value":"%s","name":"单位地址","label":"COMPANY"}]'%(f.address()),
    'name':f.name(),
    'nemail':'[{"label":"EMAIL","name":"邮箱","value":"%s"}]'%(f.ascii_email()),
    'new_company_name':'[{"label":"COMPANY","name":"公司","value":"%s"}]'%(f.company()),
    'new_position':'[{"label":"POSITION","value":"","name":"职位"}]',
    'nwebsite':'[]',
    'social':'[]',
    'tel':'[{"label":"MOBILE","value":"%s","name":"手机"}]'%(f.phone_number()),
    }

    url = 'http://yun.115rc.com/api/1.0/ios/9.0.0/22431/customer/save_member'


    r = requests.post(url=url,data=data,headers=headers)
    stat = r.json()
    print(stat)