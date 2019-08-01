import requests
import re
from pyecharts.charts import Bar
headers = {
    'Cookie':'Hm_lvt_17965aa5d4a3ebae4c8b68932b9557a8=1562639526;acw_tc=784e2c9d15640478198377695e4e9913a130171b3a1b280a6f11b928b51dd3;UID=84838689_A1_1564619000;CID=5bb50052b339dd96a134d015b0f2743f;SEID=d78cb57f6d4365014af1dd328a04969047cbd3f8096913b50448855d7560ae7a1dd1bd0b9a8d67ef1051107c9bca460127b0802a57d21bdec3f0de36;'
}

url = 'https://yun.115.com/api/1.0/web/1.0/5/news/glist?start=0&limit=20&search_user_id=&start_time=&to_time=&order=&color=1'

resq = requests.get(url=url,headers=headers)
data = resq.json()
users = data['data']['list']
user = str(users)
print(user)
name = re.findall('user_name\':\'(.*?)\'\,\'is_member',user,re.S)
print(name)
print(data['data']['list'])
print('响应解析后的类型：',type(data))
print('响应解析后的键值对个数：',len(data))
for key in data: #打印出所有的keys
    print(key ,end=' ')
