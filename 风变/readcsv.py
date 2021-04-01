import pytest
import csv

def get_data():
    with open('D:\\listtest\\风变\\test_case.csv') as f:
        list1 = csv.reader(f)
        my_data = []
        for row in list1:#得到的row是一个list
            my_data.extend(row)#把row中的list合并为一个list
        return my_data#取得所有的数据放在一个list返回
@pytest.mark.parametrize('name',get_data())
def test01(name):
   print(name)

if __name__ == '__main__':
    pytest.main(['-sv', '风变\\readcsv.py'])