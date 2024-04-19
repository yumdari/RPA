
from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹드라이버 설정 (ex. Chrome)
driver = webdriver.Chrome()

driver.get('https://www.naver.com/')

# h1 태그 모두 찾기
h1_tags = driver.find_elements(By.TAG_NAME,'div')
for tag in h1_tags:
    print(tag.text)

driver.close()