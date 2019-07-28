import requests
import re

def douban_list(url):

    html = requests.get(url).text.replace(' ', '').replace('\n', '')

    titles = re.findall('<divclass="pl2">.*?title="(.*?)">.*?<p',html,re.S)

    #trtitles = re.findall('<pclass="pl">(.*?)</p>',html,re.S)

    conturies = re.findall('<pclass="pl">(.*?)</p>',html,re.S)

    marks = re.findall('<spanclass="rating_nums">(.*?)</span>',html,re.S)

    says = re.findall('<spanclass="pl">\((.*?)人评价\)',html,re.S)

    words = re.findall('<spanclass="inq">(.*?)</span>',html,re.S)


    for title,contry,mark,say,word in zip(titles,conturies,marks,says,words):

        print(title,'\n',contry,'\n',mark,'\n',say,'\n',word,'\n')
        print('--------------------------------------------------------------------------------------')

if __name__ == "__main__":

    urls = [f'https://book.douban.com/top250?start={i}' for i in range(0, 225, 25)]

    for url in urls:
        
        douban_list(url)


