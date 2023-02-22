'''
Created on 2023. 2. 21.
if문 개념 배우기 if~elif
@author: youngmin
'''


x = 1
y = 2

if x > y: # 조건이 참이면 바로 아래 문장 실행
    print('x가 y보다 큽니다')
elif x < y: # 위 조건이 참이 아니면 아래 조건 확인 후 참이면 실행
    print('x가 y보다 작습니다')
else: # 그도 아니라면 아래 문장 실행
    print('x와 y가 같습니다.')

