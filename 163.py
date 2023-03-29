'''
Created on 2023. 3. 24.
163 URL에서 호스트 도메인 추출하기
@author: youngmin
'''

url = 'http://news.naver.com/main/read.nhn?/mode=LSD$mid=shm&sid1=105&oid=028=0002334601'

tmp = url.split('/') # /로 나눈 url만 가져온다.
domain = tmp[2] # /로 나눈 부분 중, 세 번째 브록이 도메인이다. news.naver.com
print(domain)