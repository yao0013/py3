import requests
from pyecharts.charts import Bar

headers = {
    'Cookie':'acw_tc=784e2c9715632849953358334e541710f26021b61e7425677252f9b6b8098e; UID=84838689_A1_1564663444; CID=26b465a552d8229201fc709f686c0de6; SEID=d61fe3513605ff74b511ef1316fdb1b91b8a200854c7357b6f13129f2a4a1bffd688cfefe6566ace3b07565da6be92de8edc361afc290273931b68a6'
}

url = 'https://yun.115.com/api/1.0/web/1.0/5/news/glist?start=0&limit=100&search_user_id=&start_time=&to_time=&order=&color=1'

resq = requests.get(url=url,headers=headers)
data = resq.json()
for i in range(1,100):
    users = data['data']['list'][i]['user_name']