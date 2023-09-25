import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
#To Generate Fake stuffs
from faker import Faker
fake=Faker()
driver=webdriver.Chrome()
driver.get('https://www.opencart.com')
wait=WebDriverWait(driver,20)
#Register Account
Register=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="navbar-collapse-header"]/div/a[2]')))
Register.click()

time.sleep(10)
wait=WebDriverWait(driver,10)
User_Name=driver.find_element(By.ID,'input-username')
Fake_UserName=fake.name()
User_Name.send_keys(Fake_UserName)
time.sleep(2)
wait=WebDriverWait(driver,10)
First_Name=driver.find_element(By.ID,'input-firstname')
Fake_FirstName=fake.first_name()
First_Name.send_keys(Fake_FirstName)
time.sleep(2)

Last_Name=driver.find_element(By.ID,'input-lastname')
Fake_LastName=fake.last_name()
Last_Name.send_keys(Fake_LastName)
time.sleep(2)

Email=driver.find_element(By.ID,'input-email')
Fake_Email=fake.email()
Email.send_keys(Fake_Email)
time.sleep(2)

Select_Country=Select(driver.find_element(By.ID,'input-country'))
Select_Country.select_by_visible_text('Nepal')
time.sleep(2)

Input_Password=driver.find_element(By.ID,'input-password')
Input_Password.send_keys('Test@123#')
print(Fake_Email)
print(Input_Password)
time.sleep(20)
driver.close()