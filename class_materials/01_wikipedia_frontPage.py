import re # 모듈 가져오기
import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Main_Page'

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"

headers = {"User-agent": USER_AGENT}
r = requests.get(URL, headers=headers, timeout=5)
page = r.text

soup = BeautifulSoup(page, 'html.parser') # html.parse로 page에 있는 내용을 파싱함

div = soup.find('div', id='mp-tfa') # 파싱한 내용에서 div 태그의 id가 mp-tfa인 것을 고름?

div_str = str(div) # div 태그들의 내용을 스트링으로 바꿈?

div_str = re.sub('<.*?>', '', div_str)
div_str = re.sub(' +', ' ', div_str)
div_str = re.sub('\n+', '\n', div_str)
div_str = div_str.strip()

print(div_str)
