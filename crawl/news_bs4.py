import requests
from bs4 import BeautifulSoup

def get_latest_naver_news(query, num_articles=10):
    """
    네이버 뉴스 검색 결과에서 최신 뉴스 아이템들을 가져오는 함수.

    Args:
    query (str): 검색할 쿼리.
    num_articles (int): 가져올 뉴스 아이템의 수.

    Returns:
    list: 최신 뉴스 아이템들의 제목과 URL이 담긴 리스트.
    """
    
    """
    SSL warning 방지
    """
    import urllib3
    urllib3.disable_warnings()
    
    # 네이버 뉴스 검색 URL
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query={query}"

    # 페이지 내용 가져오기
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 뉴스 아이템 추출
    news_items = soup.find_all('div', {'class': 'news_area'}, limit=num_articles)
    latest_news = []
    for item in news_items:
        title = item.find('a', {'class': 'news_tit'}).text
        link = item.find('a', {'class': 'news_tit'})['href']
        latest_news.append({'title': title, 'link': link})

    return latest_news

# 최신 10개 뉴스 아이템 가져오기
latest_news_items = get_latest_naver_news('인공지능')

# 결과 출력
for news in latest_news_items:
    print("제목: {news['title']}\n링크: {news['link']}\n")