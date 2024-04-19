from selenium import webdriver

def selenium_test():
    URL = 'https://www.google.co.kr/'
    driver = webdriver.Chrome()
    driver.get(url=URL)
    
    while(True):
        pass
    
selenium_test()