from lxml import etree
import requests

def douban_list(url):

    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    
    titles = html.xpath("//div[@class='pl2']/a/text()")

    #trtitles = html1.xpath("//tr[@class='item']/td[2]/div[@class='pl2']/span/text()")

    conturies = html.xpath("//p[@class='pl']/text()")

    marks = html.xpath("//span[@class='rating_nums']/text()")

    says = html.xpath("//span[@class='pl']/text()")

    words = html.xpath("//span[@class='inq']/text()")


    for title,contry,mark,say,word in zip(titles,conturies,marks,says,words):

        print(title,contry,mark,say,word)

        print('--------------------------------------------------------------------------------------')

if __name__ == "__main__":

    urls = [f'https://book.douban.com/top250?start={i}' for i in range(0,225,25)]

    for url in urls:
        
        douban_list(url)


