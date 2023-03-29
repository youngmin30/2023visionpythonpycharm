'''
Created on 2023. 3. 27.
172 인터넷에 있는 이미지를 내 pc로 저장하기
@author: youngmin
'''

from urllib.requet import urlopen

imgurl = 'http://www.iaidol,com/img_sample.jpg' # 이미지가 있는 경로

imgname = imgurl.split('/')[-1] # / 기준으로 나눈 것 중, 

try:
    with urlopen(imgurl) as f: # urlopne(imgurl)의 url을 열었음.
        with open(imgname, 'wb') as h: # imgname을 가져와 바이너리로 쓰기 모드로 열기
            img = f.read() # 파일을 읽음.
            h.write(img) # 이미지를 씀.
except Exception as e:
    print(e)
