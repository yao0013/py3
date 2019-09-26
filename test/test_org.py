import requests
import pytest

def get_group():
    headers = {
    'Cookie':'Hm_lvt_17965aa5d4a3ebae4c8b68932b9557a8=1562639526; acw_tc=784e2c9a15692356753077994e43bd7ec20a68c3db152d8e9303526a9bdd47; UID=84838689_A1_1569382448; CID=de2b3ab61067e8ac5fbeecc612b80d12; SEID=f14384c17893a6c27a8bb5c76fcc0636759e7c2dcb7592da032ae99c4e923dff11a0c60ea263c1f911b9e31514228d7bd71107677087a660fc3862e4'
    }

    url = 'https://yun.115.com/5/portal/groups'

    resq = requests.get(url=url,headers=headers)

    data = resq.json()

    gp = []

    for i in range(0,2):
        gp.append(data['data'][i]['gp_name'])
   
    return gp


def test_gp():
    assert '广东一一五科技股份有限公司' in get_group()

if __name__ == "__main__":
    pytest.main(['-q','test\\test_org.py','--html=report.html'])
