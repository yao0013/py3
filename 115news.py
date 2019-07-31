import requests
from pyecharts.charts import Bar
headers = {
    'Cookie':'acw_tc=784e2c9d15640478198377695e4e9913a130171b3a1b280a6f11b928b51dd3;CID=f2f6109e5dc45641b898ef899cff9f1d;Hm_lvt_17965aa5d4a3ebae4c8b68932b9557a8=1562639526;'
}

url = 'https://yun.115.com/api/1.0/web/1.0/5/news/glist?start=0&limit=20&search_user_id=&start_time=&to_time=&order=&color=1'

resq = requests.get(url=url,headers=headers)
data = resq.json()
user_name = data['data']['list']['user_name']
print(user_name)