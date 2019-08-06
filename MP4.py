import requests
from lxml import etree

def get_url(url):
    html1 = requests.get(url).text
    html = etree.HTML(html1)
    movies_name = html.xpath(
        '//div[@class="content"]/div[@class="detail"]/div[@class="box"]/div[@class="list"]/ul/li/a/@title')
    movies_url = html.xpath(
        '//div[@class="content"]/div[@class="detail"]/div[@class="box"]/div[@class="list"]/ul/li/a/@href')
    movies = list(zip(movies_name, movies_url))
    return (movies)

def get_magnet(movies):

    

    for movie in movies:

        url_2 = movie[1]

        movie_name = movie[0]

        html2 = requests.get(url=url_2).text

        html3 = etree.HTML(html2)

        magnet = html3.xpath('//*[@id="fadecon"]/div[1]/ul/li[2]/div/a/@href')

        hrefname = html3.xpath('//*[@id="fadecon"]/div[1]/ul/li[2]/div/a/text()')
        
        print(movie_name,'\n',hrefname[0],':', magnet[0],)
        print("-----------------------------------------------------------------------------")
        file = open('0804.txt','a',encoding = 'utf- 8')
        file.write(movie_name+'\n')
        file.write(hrefname[0]+':'+ magnet[0]+'\n')
    file. close()


def main():
    urls = [f'http://www.mp4ba.com/dianying/list_{i}.html' for i in range(1,10)]
    for url in urls:
        movies = get_url(url)
        get_magnet(movies)

if __name__ == '__main__':
    main()