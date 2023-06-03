import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('E:\chromedriver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element(By.XPATH, "//input[@id ='autosuggest']").send_keys('ind')
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
for country in countries:
    if country.text == 'India':
        country.click()
        break

#get attribute is used when you are passing dynamic value which is not available when  page loads for the first time 
assert(driver.find_element(By.XPATH, "//input[@id ='autosuggest']").get_attribute('value') == 'India')





