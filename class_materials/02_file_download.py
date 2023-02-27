import os
import time
import random
import re
import requests
from bs4 import BeautifulSoup

URL = 'http://www.adobe.com/investor-relations/financial-documents.html'
MIN_WAIT_TIME = 0.5
MAX_WAIT_TIME = 2
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"

outDir = 'PDF_FILES'
if not os.path.isdir(outDir):
    os.makedirs(outDir)


def getFile(url):
    while True:
        try:
            headers = {"User-agent": USER_AGENT}
            r = requests.get(url, headers=headers, timeout=20)
            content = r.content
            t = random.uniform(MIN_WAIT_TIME, MAX_WAIT_TIME)
            time.sleep(t)
            return content
        except:
            print("error!")
            print("retry...")
            time.sleep(20)


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


def getOutFn(a_href):
    title = a_href.get_text()
    title = re.sub('[^a-zA-Z0-9\s]', '', title)
    outFn = title.strip() + '.pdf'
    return outFn


def getPdfUrl(a_href):
    pdf_url = a_href.get('href')
    if pdf_url.startswith('/'):
        pdf_url = 'http://www.adobe.com{}'.format(pdf_url)

    return pdf_url


page = getPage(URL)

soup = BeautifulSoup(page, 'html.parser')

for div in soup.find_all('div', class_='Semantic LayoutCellSides LayoutBreakAfter TextSmall SemanticDC TextBreak'):
    for a_href in div.find_all(href=re.compile('\.pdf')):
        pdf_url = getPdfUrl(a_href)
        print(pdf_url)

        file_content = getFile(pdf_url)

        outFn = getOutFn(a_href)

        with open(os.path.join(outDir, outFn), 'wb') as outF:
            outF.write(file_content)