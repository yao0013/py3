from gog import ReadCsv
from token_1 import Get_token1
import requests
import json
re = ReadCsv()
q = re.read_csv()
print(q)

p1 = q[0][1]

print(p1)

t1 = Get_token1()

t1_1 = t1.get_token1()

print(t1_1)