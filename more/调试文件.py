import csv
import sys
import requests
from lxml import etree
from threading import Thread
from tkinter import messagebox
import pandas as pd
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"}
url="https://steamdb.info/upcoming/free/"
html = requests.get(url,headers = headers)

text = html.text
print(text)