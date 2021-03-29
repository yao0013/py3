import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from HTMLTestRunner import HTMLTestReport
import pyautogui as page
import random


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
for i in range(2000):
    i = i+1
    x = random.randint(0, driver.get_window_size()["width"])
    y = random.randint(0, driver.get_window_size()["height"])
    if (y <= 114):
        y = y+114
    if (y > 1036):
        y = 1000
    print(x,y,i)
    page.PAUSE = 0.005
    page.click(x,y)