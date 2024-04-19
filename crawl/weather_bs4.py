import datetime
from bs4 import BeautifulSoup
import urllib.request

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

print("\n       ※ Python Webcrawling Project 1 ※ \n ")
print('   환영합니다, ' + nowDate)
print('      오늘의 주요 정보를 요약해 드리겠습니다.\n')

# 오늘의 날씨
print('  ○>> #오늘의 #날씨 #요약 \n')
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
temps = soup.find_all('span',"blind")
cast = soup.find('span',"weather before_slash")
#print('--> 서울 날씨 : ' , temps.get_text() , '℃' , cast.get_text())

try:
    main_pack_section = soup.find("div", id="main_pack").find("section", recursive=False)
    div1 = main_pack_section.find("div")
    div2 = div1.find("div")
    div_type01 = div2.find("div", class_="type01")
    div_wrap_cont = div_type01.find("div", class_="wrap_cont")
    tit_box_strong = div_wrap_cont.find("div", class_="tit_box").find("strong")

    # Get the text inside the <strong> tag
    value = tit_box_strong.text.strip()

    print(value)
except AttributeError:
    print("Element not found. Check your XPath or the structure of the HTML.")
except Exception as e:
    print("An error occurred:", e)