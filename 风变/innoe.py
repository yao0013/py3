from gog import ReadCsv
from token_1 import Get_token1
import requests
import json
import pytest
#import jsonpath
#TODO 使用jsonpath断言
#TODO 使用csv导入各参数：进阶2，导入为参数
#TODO for循环持续进行多个用例
#TODO 使用GUI：延后吧，实现功能先
re = ReadCsv()

q = re.read_csv()

p1 = q[0][0]

print(p1)

t1 = Get_token1()

t1_1 = t1.get_token1()

print(t1_1)

def get_info():


    headers = {
            "X-Auth-Token": t1_1,"Host" : "192.168.203.38","Connection" : "keep-alive","Content-Length" : "31","Accept" : "application/json, text/javascript, */*; q=0.01","X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36","Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8","Accept-Encoding" : "gzip, deflate","Accept-Language" : "zh-CN,zh;q=0.9","Referer" :"http://192.168.203.38/portal/","Origin" : "http://192.168.203.38"
            }

    url = 'http://192.168.203.38/api/security/audit/archive/pageData.do'
    
    datas = {'page.pageNum': '1','page.pageSize': '10'}

    resq = requests.post(url=url,headers=headers,data=datas)

    #print(type(resq))

    pp = resq.json()

    #print(type(pp))

    return pp

def test_info():
    assert '\'success\': True' in str(get_info())

if __name__ == "__main__":
    pytest.main(['-q','风变\\innoe.py','--html=report1.html'])