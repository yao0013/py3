from lxml import etree
import requests,re,aiohttp,asyncio
import time

urls = [f'https://www.gushiwen.org/default_{i}.aspx' for i in range(1,10)]
sem = asyncio.Semaphore(10)

async def qs_list(url):
    with(await sem):
        async with aiohttp.ClientSession() as session:  
            async with session.request('GET', url) as resq: 
                html = await resq.read()
                titles = etree.HTML(html).xpath("//div[@class='cont']/p[1]/a/b/text()")
                times = etree.HTML(html).xpath("//p[@class='source']/a[1]/text()")
                authurs = etree.HTML(html).xpath("//p[@class='source']/a[2]/text()")
                contents = etree.HTML(html).xpath("//div[@class='cont']/div[@id]/text()")
                for title,time,authur,content in zip(titles,times,authurs,contents):
                    print(f"{title} 朝代：{time} 作者：{authur} ")
                    print(f"{content.replace('<br />','')}")
                    print("--------------------------------------------")

def main():
    loop = asyncio.get_event_loop()           # 获取事件循环
    tasks = [qs_list(url) for url in urls ]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
    loop.close()  # 关闭事件循环




'''    resq = requests.get(url = url)

    html = etree.HTML(resq.text)

    htmls = resq.text

    titles = html.xpath("//div[@class='cont']/p[1]/a/b/text()")

    times =  html.xpath("//p[@class='source']/a[1]/text()")
    
    authurs = html.xpath("//p[@class='source']/a[2]/text()")
    
    contents = re.findall('<div class="contson" id="contson.*?">(.*?)</div>',htmls,re.S)



    for title,time,authur,content in zip(titles,times,authurs,contents):
        print(f"{title} 朝代：{time} 作者：{authur} ")
        print(f"{content.replace('<br />','')}")
        print("--------------------------------------------")'''
if __name__ == '__main__':
    start = time.time()
    main()  # 调用方
    print('总耗时：%.5f秒' % float(time.time()-start))