import requests
from bs4 import BeautifulSoup
import csv


def douban_list(url):

    resq = requests.get(url = url)
    
    bful = BeautifulSoup(resq.text,'lxml')

    titles = bful.select("div.pl2")

    trtitles = bful.select("span")

    conturies = bful.select("p.pl")

    marks = bful.select("span.rating_nums")

    says = bful.select("span.pl")

    words = bful.select("span.inq")

    csv_list = [] 
    for title,trtitle,contry,mark,say,word in zip(titles,trtitles,conturies,marks,says,words):
        
        info = [
            title.get_text().replace(' ', '').replace('\n', ''),

            trtitle.get_text().replace(' ', '').replace('\n', ''),

            contry.get_text().replace(' ', '').replace('\n', ''),

            mark.get_text().replace(' ', '').replace('\n', ''),

            say.get_text().replace(' ', '').replace('\n', ''),

            word.get_text().replace(' ', '').replace('\n', '')
        ]
        #print(title,'\n',trtitle,'\n',contry,'\n',mark,'\n',say,'\n',word,'\n')
        #print('--------------------------------------------------------------------------------------')
        csv_list.append(info)
    return(csv_list)

def write_list(info_list):
    for info in info_list:
        with open ('0807.csv', 'a+', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow(info)

if __name__ == "__main__":
    with open ('0807.csv', 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        headers = ['书名','信息','评分','评价数','金句']
        writer.writerow(headers)
    
    urls = [ f'https://book.douban.com/top250?start={i}' for i in range(0, 225, 25) ]
    for url in urls:
        info_list = douban_list(url)
        write_list(info_list)
