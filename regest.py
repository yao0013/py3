import requests

def regedit():
    name = str(input('请输入注册名'))
    data = {
    'username':name
    }

    headers = {
    'cookie':'Hm_lpvt_3b0150c3aee6054cf944ea6c8f8a7392=1569547590; Hm_lvt_3b0150c3aee6054cf944ea6c8f8a7392=1569547590'
    }

    url = 'https://www.charles.ren/api/licenseKey/generate'

    r = requests.post(url=url,headers=headers,data=data)
    back = r.json()['data']

   
    print(f'注册码是{back}')

regedit()