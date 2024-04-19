from selenium import webdriver
from selenium.webdriver.common.by import By

import time

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get('https://naver.com/')

driver.find_element(By.XPATH, '//*[@id="account"]/div/a').click()

time.sleep(1)

driver.close()