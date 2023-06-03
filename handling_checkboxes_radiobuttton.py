import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('E:\chromedriver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        time.sleep(2)
        assert(checkbox.is_selected())
        break


#handling radio buttons

radios = driver.find_elements(By.XPATH, "//input[@type='radio']")
for radio in radios:
    if radio.get_attribute('value') == 'radio2':
        radio.click()
        time.sleep(2)
        assert(radio.is_selected())
        break
