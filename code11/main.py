import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.fastcampus.co.kr/dev_online_introdev/#row_course"

rq = rquests.get(URL)
soup = bs(rq.content, 'html.parser')
# 개발자 도구를 통한 웹사이트 분석

# 크롤링 코드 작성

# 파일 저장 및 데이터 분석