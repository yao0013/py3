import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from HTMLTestRunner import HTMLTestReport
import pyautogui as page
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 


options = webdriver.ChromeOptions()

options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(executable_path='d:\py3\chromedriver.exe',chrome_options=options)

driver.maximize_window()

driver.get('https://192.168.215.44:17810/#/user/login')

time.sleep(2)

user = driver.find_element_by_id('username')
user.send_keys('admin')
password = driver.find_element_by_id('password')
password.send_keys('123456')
button = driver.find_element_by_xpath("/html//form[@id='formLogin']/div[5]//button[@type='submit']")
button.click()
time.sleep(10)

length = len(driver.find_elements_by_class_name("title"))

for i in range(0,1000):
    a = random.randint(0,length)
    links = driver.find_elements_by_class_name("title")
    link = links[a]
    link.click()
    time.sleep(1)
    driver.back()
    print(i)
    time.sleep(2)