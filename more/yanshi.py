import time
from selenium import webdriver

driver = webdriver.Chrome('d:\py3\chromedriver.exe')

driver.maximize_window()

driver.get('http://192.168.203.38/portal/#/login')

time.sleep(5)
driver.switch_to.frame(driver.find_elements_by_xpath("/html/body/iframe"))
user = driver.find_elements_by_xpath("/html/body/div[@id='app']/div[@class='container']/div[@class='login-panel']/div[@class='login_form']/form[@class='ivu-form ivu-form-label-right']/div[@class='area username']/div[@class='ivu-form-item']/div[@class='ivu-form-item-content']/input[@class='login-field username']")
user.send_keys("admin")
time.sleep(5)