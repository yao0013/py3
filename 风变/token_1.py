from gog import ReadCsv
import requests
import json
class Get_token1():

    def get_token1(self):

        headers = {
            "Host" : "192.168.203.38","Connection" : "keep-alive","Content-Length" : "31","Accept" : "application/json, text/javascript, */*; q=0.01","X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36","Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8","Accept-Encoding" : "gzip, deflate","Accept-Language" : "zh-CN,zh;q=0.9","Referer" :"http://192.168.203.38/portal/","Origin" : "http://192.168.203.38"
            }

        url = 'http://192.168.203.38/api/portal/identity/user/login.sso'
    
        datas = {'loginName': 'admin','password': '123456'}

        resq = requests.post(url=url,headers=headers,data=datas)

        data1 = resq.json()

        token_id=data1['token']

        return token_id