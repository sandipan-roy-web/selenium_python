import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('E:\chromedriver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.CSS_SELECTOR,"#name").send_keys('Sandipan')
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
name='Sandipan'
alert = driver.switch_to.alert
print(alert.text)
assert name in alert.text
alert.accept()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR , '#confirmbtn').click()
all = driver.switch_to.alert
print(all.text)
all.dismiss()
time.sleep(2)
