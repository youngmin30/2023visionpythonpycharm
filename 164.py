'''
Created on 2023. 3. 24.
164 URL에서 쿼리 문자열 추출하기
@author: youngmin
'''

url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601'

tmp = url.split('?') # ?로 나눈 부분을 tmp에 저장
queries = tmp[1].split('&') # &으로 나눈 부분을 queries에 저장
for query in queries: # tmp는 버리고, query만 출력
    print(query)
