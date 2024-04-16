
from selenium import webdriver

# 웹드라이버 설정 (ex. Chrome)
driver = webdriver.Chrome('C:/Users/hun/Downloads/chromedriver-win64chromedriver/chromedriver.exe')

driver.get('https://www.naver.com/')

# h1 태그 모두 찾기
h1_tags = driver.find_elements_by_tag_name('div')
for tag in h1_tags:
    print(tag.text)

driver.close()

'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = 'C:/Users/hun/Downloads/chromedriver-win64chromedriver/chromedriver.exe'
service = Service(executable_path=CHROME_DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://www.naver.com/')
'''