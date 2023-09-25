from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
fake=Faker()
import random

driver=webdriver.Chrome()
driver.get('https://www.opencart.com')
driver.maximize_window()
#Login to OpenCart
Login_URL=driver.find_element(By.LINK_TEXT,'Login')
Login_URL.click()
time.sleep(5)
User_Email=driver.find_element(By.ID,'input-email')
User_Email.send_keys('mbdds54@gmail.com')
time.sleep(2)
User_Password=driver.find_element(By.ID,'input-password')
User_Password.send_keys('Test@123#')
time.sleep(2)
Login_Button=driver.find_element(By.XPATH,'//*[@id="account-login"]/div[2]/div/div[1]/form/div[3]/div[1]/button[1]')
Login_Button.click()
time.sleep(10)
print('Welcome to OpenCart!!')
driver.close()