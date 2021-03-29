import requests
import pymongo
import time

client = pymongo.MongoClient(host= 'localhost',port=27017)
db = client.test
collection = db.priv115for360


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; ZUK Z1 Build/MMB29M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30;360appstore'
}
def get_info(url):
    resq = requests.get(url=url,headers=headers)
    data = resq.json()


    for i in range(0,13):
        usernames = data['data']['messages'][i]['username']
        talks = data['data']['messages'][i]['content']
        scores = data['data']['messages'][i]['score']
        datas = {'username':usernames,'talks':talks,'scores':scores}
        print(datas)
        writer_mongo(datas)   

def writer_mongo(datas):
    collection.insert_one(datas)

if __name__ == '__main__':
    urls = [f'https://comment.mobilem.360.cn/comment/getComments?baike=1034&level=0&start={i}&count=10&topLike=1&os=23&os_version=6.0.1&vc=300080105&v=8.1.5&md=ZUK+Z1&sn=4.589389937671455&cpu=qualcomm+msm8974pro-ac&ca1=armeabi-v7a&ca2=armeabi&m=c0ffe191114a311b3a58e58c9df32779&m2=e2f80771015cf9daa44b7cf71411d44a&ch=710940&ppi=1080_1920&startCount=1&pvc=455&pvn=4.5.5&re=3116&tid=0&cpc=1&snt=-1&nt=1&gender=1&age=24&newuser=1&theme=2&br=ZUK&carrier_id=70123&mac=775507e7dab440fd9480216ed68e2b60&androidid=4451724f22b76d70&serialno=c265ec93&s_3pk=1&webp=1'for i in range(0,1500,13)]
    for url in urls:
        get_info(url)
        time.sleep(1)
