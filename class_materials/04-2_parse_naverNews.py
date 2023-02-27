import re, os # 모듈 가져오기
from bs4 import BeautifulSoup
import html

inDir = 'NAVER_NEWS_HTML' # 디렉토리 만들고, 이름 지정
outDir = 'NAVER_NEWS_TXT'

if not os.path.isdir(outDir): # 만약 디렉토리가 없으면, 위에서 정한 ourDir를 넣음
    os.makedirs(outDir) #


# getTxtElm
def getTxtElm(p, txt):
    m = re.search(p, txt, re.S) # re.search(pattern, string)
    if m:
        elm = m.group(1)
    else:
        elm = ''
    return elm.strip()

# getTitle
def getTitle(soup):
    title = soup.find('meta', property='og:title')
    title = title.get('content')
    title_str = str(title)
    title_str = html.unescape(title_str)
    return title_str

# getUrl
def getUrl(soup):
    url = soup.find('meta', property='og:url')
    url = url.get('content')
    return url

# getDate
def getDate(html_txt):
    date = getTxtElm('기사입력 ([0-9\.]+)', html_txt)
    date = date.replace('.', '-')
    if date == '':
        date = getTxtElm('기사입력 <span class="t11">([0-9\-]+)', html_txt)

    return date

# getBody
def getBody(soup):
    div = soup.find('div', class_='news_end')
    if div is None:
        div = soup.find('div', id='articleBodyContents')
    div_str = str(div)
    div_str = re.sub('<em class="img_desc">(.*?)</em>', '', div_str)
    div_str = re.sub("<br ?/?>", "\n", div_str)
    div_str = re.sub('<p class="source">.*?</p>', '', div_str)
    div_str = re.sub('<.*?>', '', div_str)
    div_str = re.sub('\n+', '\n', div_str)

    return html.unescape(div_str.strip())


for dn, dns, fns in os.walk(inDir):
    for fn in fns:
        with open(os.path.join(dn,fn), 'r', encoding='utf8') as inF:
            html_txt = inF.read()

        soup = BeautifulSoup(html_txt, 'html.parser')

        url = getUrl(soup)
        title = getTitle(soup)
        date = getDate(html_txt)
        body = getBody(soup)

        xml = '<url>{}</url>\n<title>{}</title>\n<date>{}</date>\n<body>\n{}\n</body>\n'.format(url, title, date, body)

        with open(os.path.join(outDir,fn.replace('.html', '.txt')), 'w', encoding='utf8') as outF:
            outF.write(xml)