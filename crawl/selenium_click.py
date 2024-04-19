from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://naver.com/')

driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()