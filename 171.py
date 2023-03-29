'''
Created on 2023. 3. 27.
171 URL에 접속하여 HTML 페이지를 파일로 저장히기
@author: youngmin
'''

from urllib.requet import urlopen

url = 'https://www.python.org/'

with urlopen(url) as f:
    doc = f.read().decode()
    with open('pythonhome.html', 'w') as h:
        h.writelines(doc)
