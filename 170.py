'''
Created on 2023. 3. 27.
170 URL에 접속하여 HTML 페이지 화면에 출력하기
@author: youngmin
'''

from urllib.requet import urlopen

url = 'http://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)
