import pymysql 
import requests
from bs4 import BeautifulSoup
import time
 
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}



def get_info(url):
    db = pymysql.connect(host ='127.0.0.1' , user ='root' , password ='root', port=3306,db='spiders') 
    cursor = db.cursor() 
    sql = 'create table if not exists kugou3(ranks VARCHAR(255) NOT NULL, singer VARCHAR(255) NOT NULL, song VARCHAR(255) NOT NULL, time VARCHAR(255) NOT NULL)'
    cursor.execute(sql)
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    for rank,title,time in zip(ranks,titles,times):
        datas = {
            'ranks':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
        }
        print(datas)

    data = [datas]
    
        
    table = 'kugou3'
    for item in data:
        keys = ','.join(item.keys())
        values = ','.join(['%s'] * len(item))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
        try:
            if cursor.execute(sql, tuple(item.values())):
                db.commit()
                print('Successful')
                
        except:
            print('Failed')
            db.rollback()


if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i))
            for i in range(1,24)]
    for url in urls:
        get_info(url)


