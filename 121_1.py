'''
Created on 2023. 2. 28.
121 리스트의 모든 요소의 합 구하기(sum)
모듈명은 숫자로 하지 않기 오류 생김
@author: youngmin
'''

listData = range(1, 1000001) # 1부터 백만까지의 리스트

hap = 0;

for x in listData:
    hap += x # 여기도 문장 끝 나타낼 때 ; 써도 되고 그렇지 않아도 된다.
    
print(f'1~100만까지의 합은 {hap}입니다.')
print(f'1부터 백만까지의 합은 {sum(listData)}입니다.') # 이곳에서 바로 계산됨