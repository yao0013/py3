import time
from selenium import webdriver

driver = webdriver.Chrome('d:\py3\chromedriver.exe')

driver.maximize_window()

driver.get('http://192.168.203.171/login.html')

time.sleep(2)

user = driver.find_element_by_id('user')
user.send_keys('ad2019')
password = driver.find_element_by_id('password')
password.send_keys('123qweQWE')
button = driver.find_element_by_xpath("/html/body/div[@class='m-login-bg']/div[@class='m-login']/div[@class='m-login-warp']/form[@class='layui-form']/div[@class='layui-form-item m-login-btn']/div[@class='layui-inline']/button[@class='layui-btn layui-btn-warm']")
button.click()
time.sleep(5)
list1 = driver.find_element_by_id('jq3')
list1.click()
time.sleep(5)
list2 = driver.find_element_by_xpath("/html/body/div[@id='main-layout']/div[@class='main-layout-side']/ul[@id='menutree']/li[@id='jq3']/dl[@class='layui-nav-child']/dd[@class='lm13']/a")
list2.click()
time.sleep(5)
'''driver.switch_to.frame(driver.find_elements_by_name("iframeF010101"))
driver.switch_to.frame(driver.find_elements_by_xpath("/html/body/div/div/div[1]/iframe"))
input1 = driver.find_elements_by_xpath("/html/body/div[1]/form/div/div[2]/div[1]/input")
input1.send_keys('1234567890123456789012345678')
serchbut = driver.find_elements_by_xpath("/html/body/div[@id='app']/form[@class='layui-form']/div[@class='searchctr']/div[@class='searchContent']/div[@class='layui-btn-group']/button[@class='layui-btn layui-btn-normal']")
serchbut.click()
time.sleep(5)'''

js='window.open("http://192.168.203.171/system/dispather/index?url=control/service-register_z");'
driver.execute_script(js)
time.sleep(5)
input1 = driver.find_elements_by_xpath("/html/body/div[@id='app']/form[@class='layui-form']/div[@class='searchctr']/div[@class='searchContent']/div[@class='layui-inline flexBox']/input[@class='layui-input']")
input1.send_keys('123456789012345678901234567890')
serchbut = driver.find_elements_by_xpath("/html/body/div[@id='app']/form[@class='layui-form']/div[@class='searchctr']/div[@class='searchContent']/div[@class='layui-btn-group']/button[@class='layui-btn layui-btn-normal']")
serchbut.click()
time.sleep(5)