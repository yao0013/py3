import requests
import pytest
import pandas

def get_info():
    headers = {
        "Host" : "192.168.203.38","Connection" : "keep-alive","Content-Length" : "31","Accept" : "application/json, text/javascript, */*; q=0.01","X-Auth-Token" : "4bc714e7-6e89-3c3f-8182-eda2aefe99f6","X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36","Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8","Accept-Encoding" : "gzip, deflate","Accept-Language" : "zh-CN,zh;q=0.9"
    }

    url = 'http://192.168.203.38/api/security/crawler/vulnerability/search.do'
    
    datas = {'page.pageNum': '1','page.pageSize': '10'}

    resq = requests.post(url=url,headers=headers,data=datas)

    data1 = resq.json()

    gp = []

    for i in range(0,2):
        gp.append(data1['data']['list'][i]['info'])
   
    return gp


def test_info():
    assert 'OpenSSL 安全漏洞' in get_info()

if __name__ == "__main__":
    pytest.main(['-q','test\\test_001.py','--html=report1.html'])

