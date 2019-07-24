import requests
from bs4 import BeautifulSoup

def scgf_list(url):

    resq = requests.get(url)
    
    bful = BeautifulSoup(resq.text,'lxml')

    titles = bful.select("b")

    tandas = bful.select("p.source")

    contens = bful.select("div.contson")

    for title,tanda,conten in zip(titles,tandas,contens):
        
        title = title.get_text().strip()

        tanda = tanda.get_text().strip()

        conten = conten.get_text().strip()

        print(title,'\n',tanda,'\n',conten,'\n')
        print('--------------------------------------------------------------------------------------')

if __name__ == "__main__":

    urls = [f'https://www.gushiwen.org/default_{i}.aspx' for i in range(1,10)]

    for url in urls:
        
        scgf_list(url)


