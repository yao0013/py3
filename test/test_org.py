import requests


headers = {
    'Cookie':'Hm_lvt_17965aa5d4a3ebae4c8b68932b9557a8=1562639526; acw_tc=784e2c9d15640478198377695e4e9913a130171b3a1b280a6f11b928b51dd3; UID=84838689_A1_1564712498; CID=f7c3fb1f3a71ae496872f6ab1c091f99; SEID=453002d6ec30fb8f73d18be51417e94afb14c8882bea0c1c6369acb750475093af98802e75de81e9627e9365451f4f663a1b8802aa2325c40a5e1d0a'
}

url = 'https://yun.115.com/api/1.0/web/1.0/5/contact/get_list?keyword=&start=0&limit=300'

resq = requests.get(url=url,headers=headers)

data = resq.json()

gender = []

for i in range(0,263):
    gender.append(data['data']['list'][i]['gender'])

dic = []

set_list = set(gender)


for item in set_list:
    dic.append(gender.count(item))

