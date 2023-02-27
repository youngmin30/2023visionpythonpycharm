import time
import random
import re
import requests
from bs4 import BeautifulSoup

URL_TMPL = 'http://movie.naver.com/movie/point/af/list.nhn?&page={}'
MIN_WAIT_TIME = 0.5
MAX_WAIT_TIME = 2
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"

def getPage(url):

    try:
        headers = {"User-agent": USER_AGENT}
        r = requests.get(url, headers=headers, timeout=5)
        page = r.text
        t = random.uniform(MIN_WAIT_TIME, MAX_WAIT_TIME)
        time.sleep(t)
        return page
    except:
        time.sleep(20)


def getTxtElm(p, txt):
    m = re.search(p, txt, re.S)
    if m:
        elm = m.group(1)
    else:
        elm = ''
    return elm.strip()


for pageNum in range(1,10):

    url = URL_TMPL.format(pageNum)
    page = getPage(url)

    soup = BeautifulSoup(page, 'html.parser')

    tb = soup.find('table', class_='list_netizen')
    tbody = tb.find('tbody')

    for tr in tbody.find_all('tr'):
        mv_tit = tr.find('a', class_='movie').get_text()
        point = tr.find('td', class_='point').get_text()
        cmt = getTxtElm('<br>(.*?)<', str(tr))

        print(mv_tit, point, cmt)