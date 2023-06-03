from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service('E:\chromedriver\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service = service_obj)
driver.get('https://pypi.org/project/selenium')
print(driver.current_url)
print(driver.title)
driver.close()
