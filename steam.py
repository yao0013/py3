import csv
import sys
import requests
from lxml import etree
from threading import Thread
from tkinter import messagebox
import pandas as pd
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}

def login(url="https://steamdb.info/upcoming/free/"):
    try:
        html = requests.get(url,headers = headers)
        if html.status_code == 200:
            text = html.text
            print(text)
            dom = etree.HTML(text)
            return dom
        else:
            pass
    except:
        messagebox.showinfo("warning","warn Internet")
        sys.exit(0)
def now(dom):
    name = dom.xpath('//table[1]//a/b/text()')
    price = dom.xpath('//table[1]//td[4]/text()')
    start_time = dom.xpath('//table[1]//td[5]/@title')
    end_time = dom.xpath('//table[1]//td[6]/@title')
    for a,b,c,d in zip(name,price,start_time,end_time):
        name,price,start,end = replace(a,b,c,d)
        write_csv(name,price,start,end,"now.csv")
def furture(dom):
    name = dom.xpath('//table[2]//a/b/text()')
    price = dom.xpath('//table[2]//td[3]/text()')
    start_time = dom.xpath('//table[2]//td[4]/@title')
    end_time = dom.xpath('//table[2]//td[5]/@title')
    for a,b,c,d in zip(name,price,start_time,end_time):
        name,price,start,end = replace(a,b,c,d)
        write_csv(name,price,start,end,"furture.csv")
def replace(name,price,start,end):
    start = start.split("+")[0]
    end = end.split("+")[0]
    if price != "Weekend":
        name = name.split("Limited")[0]
        price = "Free"
    else:
        name = name.split("Free")[0]
    return name,price,start,end
def write_csv(name,price,start,end,csv_name):
    with open(csv_name,"a",newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([name,price,start,end])
    print(name,price,start,end)
def read_csv(csv_name):
    url = "https://store.steampowered.com/search/?term="
    csv_data = pd.read_csv(csv_name,header = None,encoding = "utf-8")
    names = csv_data[0]
    start_times = csv_data[2]
    end_times = csv_data[3]
    count = 1
    for name,start_time,end_time in zip(names,start_times,end_times):
        name = name[:-1]
        new_name = "+".join(name.split())
        dom = login(url+new_name)
        store_name = dom.xpath('//*[@id="search_resultsRows"]/a[1]/div[2]/div[1]/span/text()')[0]
        if name == store_name:
            count += 1
            store = dom.xpath('//*[@id="search_resultsRows"]/a[1]/@href')[0]
            start_time = "日".join("月".join(start_time.split("-")[1:]).split("T"))
            end_time = "日".join("月".join(end_time.split("-")[1:]).split("T"))
            write_txt("【"+name+"】\t领取时间为：{}-{}\n".format(start_time,end_time))
            write_txt("领取地址为:{}\n".format(store))
            write_txt("{}\n".format("-"*80))
            print("写入{}次".format(count-1))
        else:
            count += 1
            write_txt("第{}项出错，请去csv内部检测\n".format(count-1))
            write_txt("游戏名字为:{}".format(name))
            write_txt("{}\n".format("-"*80))
def write_txt(text):
    with open("steam.txt","a") as f:
        f.write(text)
def run_write(csv_name):
    read_csv(csv_name)
    write_txt("-"*40,"这里是分割线","-"*40)
if __name__ == "__main__":
    threads = []
    dom = login()
    threads.append(Thread(target=now,args=(dom,)))
    threads.append(Thread(target=furture,args=(dom,)))
    for thread in threads:
        thread.start()
        thread.join()
    run_write("now.csv")
    run_write("furture.csv")