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

    csv_list = {}
    for title,trtitle,contry,mark,say,word in zip(titles,trtitles,conturies,marks,says,words):
        
        title = title.get_text().replace(' ', '').replace('\n', '')

        trtitle = trtitle.get_text().replace(' ', '').replace('\n', '')

        contry = contry.get_text().replace(' ', '').replace('\n', '')

        mark = mark.get_text().replace(' ', '').replace('\n', '')

        say = say.get_text().replace(' ', '').replace('\n', '')

        word = word.get_text().replace(' ', '').replace('\n', '')

        #print(title,'\n',trtitle,'\n',contry,'\n',mark,'\n',say,'\n',word,'\n')
        #print('--------------------------------------------------------------------------------------')
        csv_list.set(title,contry,mark,say,word)

if __name__ == "__main__":

    urls = [f'https://book.douban.com/top250?start={i}' for i in range(0, 225, 25)]

    for url in urls:
        
        douban_list(url)


