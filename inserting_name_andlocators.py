from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service('E:\chromedriver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.rahulshettyacademy.com/angularpractice/')
driver.find_element(By.NAME, "email").send_keys('sandipan84@gmail.com')
driver.find_element(By.ID, 'exampleInputPassword1').send_keys('sandip123')
driver.find_element(By.XPATH, "//input[@type ='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(message)
assert 'Success!' in message
driver.find_element(By.XPATH,"//input[@class='ng-untouched ng-pristine ng-valid']").send_keys('ss')
driver.find_element(By.XPATH,"//input[@id ='inlineRadio1']").click()
