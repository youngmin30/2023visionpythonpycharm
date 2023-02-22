'''
Created on 2023. 2. 21.
for문 개념 배우기
@author: youngmin
'''


scope = [1, 2, 3, 4, 5]

for x in scope:
    print(x)
    
    
# for 변수 in 범위:
#     반복으로 실행할 코드

# for문의 범위: 시퀀스 자료형, 반복 가능한 자료형(문자열, 리스트, 튜플, 사전, range(), 그 외 반복이 가능한 객체


# for문, 문자열
str = 'abcedf'
for c in str:
    print(c)
    
# for문, 리스트
list= [1, 2, 3, 4, 5]
for c in list:
    print(c)
    
    
# 사전(dictionary)을 범위로 지정한 예
ascii_codes = {'a':97, 'b':98, 'c':99} # key에 문자, 숫자 모두 가능함.
for c in ascii_codes:
    print(c)
    

# range() 함수를 범위로 지정한 예
for c in range(10): # 0부터 9까지
    print(c)

for c1 in range(1, 10): # 1부터 10까지
    print(c1)




    
    