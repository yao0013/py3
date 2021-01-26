import time
from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(executable_path='d:\py3\chromedriver.exe',chrome_options=options)

driver.maximize_window()

driver.get('https://192.168.215.44:17810/#/user/login')

time.sleep(2)

user = driver.find_element_by_id('username')
user.send_keys('yaocm@g-cloud.com.cn')
password = driver.find_element_by_id('password')
password.send_keys('gcloud123!@#')
button = driver.find_element_by_xpath("/html/body[@class='userLayout']/div[@id='app']/div[@id='userLayout']/div[@class='container']/div[@class='main']/div[@class='wrapper']/div[@class='container']/form[@id='formLogin']/div[@class='ant-row ant-form-item']/div[@class='ant-col ant-form-item-control-wrapper']/div[@class='ant-form-item-control']/span[@class='ant-form-item-children']/button[@class='login-button btn-transition ant-btn ant-btn-primary ant-btn-round ant-btn-lg']")
button.click()
time.sleep(5)
'''list1 = driver.find_element_by_id('jq3')
list1.click()
time.sleep(5)
list2 = driver.find_element_by_xpath("/html/body/div[@id='main-layout']/div[@class='main-layout-side']/ul[@id='menutree']/li[@id='jq3']/dl[@class='layui-nav-child']/dd[@class='lm13']/a")
list2.click()
time.sleep(5)
driver.switch_to.frame(driver.find_elements_by_name("iframeF010101"))
driver.switch_to.frame(driver.find_elements_by_xpath("/html/body/div/div/div[1]/iframe"))
input1 = driver.find_elements_by_xpath("/html/body/div[1]/form/div/div[2]/div[1]/input")
input1.send_keys('1234567890123456789012345678')
serchbut = driver.find_elements_by_xpath("/html/body/div[@id='app']/form[@class='layui-form']/div[@class='searchctr']/div[@class='searchContent']/div[@class='layui-btn-group']/button[@class='layui-btn layui-btn-normal']")
serchbut.click()
time.sleep(5)

js='window.open("http://192.168.203.171/system/dispather/index?url=control/service-register_z");'
driver.execute_script(js)
time.sleep(5)
input1 = driver.find_elements_by_xpath("/html/body/div[@id='app']/form[@class='layui-form']/div[@class='searchctr']/div[@class='searchContent']/div[@class='layui-inline flexBox']/input[@class='layui-input']")
input1.send_keys('123456789012345678901234567890')
serchbut = driver.find_elements_by_xpath("/html/body/div[@id='app']/form[@class='layui-form']/div[@class='searchctr']/div[@class='searchContent']/div[@class='layui-btn-group']/button[@class='layui-btn layui-btn-normal']")
serchbut.click()
time.sleep(5)'''