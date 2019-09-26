import requests

def regedit():
    name = input('请输入注册名')
    data = {
    'username':'%s'%name,
    }

    headers = {
    'cookie':'Hm_lvt_3b0150c3aee6054cf944ea6c8f8a7392=1569506539,1569506590; Hm_lpvt_3b0150c3aee6054cf944ea6c8f8a7392=1569506590',
    }

    url = 'https://www.charles.ren/'

    r = requests.post(url=url,headers=headers,data=data)

    back = r.json()['data']
    print(back)

regedit()