from selenium import  webdriver 
import time
from bs4 import BeautifulSoup

'''chrome_options = Options() # 实例化Option对象
chrome_options.add_argument('--headless') # 对浏览器的设置
driver = RemoteWebDriver("http://chromedriver.python-class-fos.svc:4444/wd/hub", chrome_options.to_capabilities()) # 声明浏览器对象'''
driver = webdriver.Chrome() 
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待两秒

labels = driver.find_elements_by_tag_name('label') # 根据标签名提取所有元素
#print(type(labels)) # 打印labels的数据类型
for label in labels: # 循环，遍历labels这个列表
    print(label.text) # 打印labe的文本
driver.close() # 关闭浏览器
driver.close() # 关闭浏览器