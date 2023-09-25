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

#Homepage of OpenCart. Exploring of Opencart HomePage
driver=webdriver.Chrome()
driver.get('https://www.opencart.com')
driver.maximize_window()
time.sleep(5)
Click_HomePage=driver.find_element(By.XPATH,'/html/body/header/nav/div/div[1]/a/img')
Click_HomePage.click()
#To Scroll upto Footer
initial_height = driver.execute_script("return document.body.scrollHeight")

# Set a variable for the scroll position
scroll_position = 0

# Define the scroll increment (e.g., scrolling down by 500 pixels)
scroll_increment = 200

# Scroll down until the bottom of the page is reached
while scroll_position < initial_height:
    # Scroll down by the defined increment
    driver.execute_script(f"window.scrollBy(0, {scroll_increment})")

    # Update the scroll position
    scroll_position += scroll_increment

    # Wait for a brief moment (optional)
    driver.implicitly_wait(3)
time.sleep(5)
#Contact Us in the Footer
Contact_Us=driver.find_element(By.XPATH,'/html/body/footer/div/div[1]/div[2]/section/ul/li[1]/a')
Contact_Us.click()
time.sleep(3)
#Contact Us Form
Input_Reason=Select(driver.find_element(By.ID,'input-reason'))
Input_Reason.select_by_visible_text('I would like to report an account issue')
time.sleep(2)
Reporter_Name=driver.find_element(By.ID,'input-name')
Fake_Name=fake.name()
Reporter_Name.send_keys(Fake_Name)
time.sleep(2)
Reporter_Email=driver.find_element(By.ID,'input-email')
Fake_Email=fake.email()
Reporter_Email.send_keys(Fake_Email)
time.sleep(2)
Message=driver.find_element(By.ID,'input-enquiry')
#To Generate Dummy Text..
Dummy_Message=fake.text()
Message.send_keys(Dummy_Message)
time.sleep(20)
driver.execute_script("window.scrollBy(0, 300)")
Send_Message=driver.find_element(By.ID,'button-send')
Send_Message.click()
Click_Features=driver.find_element(By.XPATH,'//*[@id="navbar-collapse-header"]/ul/li[1]/a')
Click_Features.click()
driver.execute_script("window.scrollBy(0, 200)")
time.sleep(5)
Download=driver.find_element(By.XPATH,'//*[@id="navbar-collapse-header"]/ul/li[5]/a')
Download.click()
Download_OpeCart_Zip=driver.find_element(By.XPATH,'//*[@id="cms-download"]/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/div[1]/div/a/img')
Download_OpeCart_Zip.click()
time.sleep(30)
print(Fake_Email)
driver.close()