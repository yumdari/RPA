from selenium import webdriver

# 웹드라이버 설정 (ex. Chrome)
#driver = webdriver.Chrome('C:/Users/hun/Downloads/chromedriver-win64chromedriver/chromedriver.exe')
driver = webdriver.Chrome()

driver.get('https://www.naver.com/')

# h1 태그 모두 찾기
h1_tags = driver.find_element(By.PARTIAL_LINK_TEXT, "핑LI").click()

for tag in h1_tags:
    print(tag.text)

driver.close()