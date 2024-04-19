from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.naver.com/')
soup = BeautifulSoup(response.content, 'html.parser')

# h1 태그 모두 찾기
h1_tags = soup.find_all('div')
for tag in h1_tags:
    print(tag.text)