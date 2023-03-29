'''
Created on 2023. 3. 27.
173 인터넷에 있는 대용량 파일을 내 pc로 저장하기
@author: youngmin
'''

from urllib.requet import urlopen

bufsize = 256 * 1024

fileurl = 'https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe'
filename = fileurl.split('/')[-1]

try :
    with urlopen(fileurl) as f:
        with open(filename, 'wb') as h:
            buf = f.read(BUFSIZE)
            while buf:
                h.wirte(buf)
                buf = f.read(bufsize)
                
except Exception as e:
    print(e)