import requests
import pytest

def get_group():
    headers = {
    'Cookie':'acw_tc=784e2c9c15690777587752979e78f7b4ff102a05ee32ecf233a48e8bb39be5; UID=84838689_A1_1569336964; CID=925648400cb421969824dcc4ddaa6a62; SEID=a4c9a6902cdc5892974440f50db959c27932d0587c4533b4c4f6d724d56ad359456fd47ff040aa554bda0c0103ff8313394e44fcb6eba00650a29847'
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
    pytest.main(['-q','test_org.py','--html=report.html'])

