import pymysql 
import requests
from bs4 import BeautifulSoup
import time
 
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}
 
def get_info(url):
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    times = soup.select('span.pc_temp_tips_r > span')
    for rank,title,time in zip(ranks,titles,times):
        data = {
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
        }
        print(data)

db = pymysql.connect(host ='127.0.0.1' , user ='root' , password ='root', port=3306) 
cursor = db.cursor() 
cursor.execute("use spiders") 
cursor.execute("""CREATE TABLE kugou (
         rank  CHAR(20),
         singer  CHAR(20),
         song CHAR(20),  
         dt CHAR(20))""")
db.close()

if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i))
            for i in range(1,24)]
    for url in urls:
        get_info(url)
        time.sleep(1)

