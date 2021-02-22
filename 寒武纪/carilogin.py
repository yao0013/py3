import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from HTMLTestRunner import HTMLTestReport



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
button = driver.find_element_by_xpath("/html//form[@id='formLogin']/div[5]//button[@type='submit']")
button.click()
time.sleep(5)
'''users = driver.find_element_by_xpath("/html/body/div[@id='app']/section[@class='layout bg-color ant-layout']/section[@class='ant-layout bg-color sidemenu content-width-Fixed']/header[@class='ant-layout-header ant-header-side-opened']/div[@class='header']/div[@class='user-wrapper vertical-center']/a[@class='header-btn vertical-center']/span[@class='header-underline-btn']").text'''
time.sleep(5)
r1 = EC.title_is('Cambricon AI Repo')(driver)
r2 = EC.title_contains('Cambricon AI Repo')(driver)
r3 = EC.text_to_be_present_in_element((By.CLASS_NAME,'pr6'),'塔比特')(driver)
print (r1)
print (r2)
print (r3)

with open('./HwTestReport.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='HwTestReport 测试',
                                description='带饼图，带详情',
                                tester='Johnny')
        '''runner.run(r1,r2,r3)'''
driver.quit()

'''if users == user2
    pass
else:
    raise AssertionError'''
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