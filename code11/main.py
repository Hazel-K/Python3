import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.fastcampus.co.kr/dev_online_introdev/#row_course"

rq = rquests.get(URL)
soup = bs(rq.content, 'html.parser')