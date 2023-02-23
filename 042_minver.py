'''
Created on 2023. 2. 23.
함수 리턴값 이해하기
@author: youngmin
'''

# 함수 정의(함수를 만듦) revers()
def reverse(x, y, z):
    return z, y, x


# 위에서 만든 함수 사용 revers()
ret = reverse(1, 2, 3) # 변수 하나에 세 값을 튜플로 지정, 값은 숫자
print(ret) # 값을 튜플로 출력

r1, r2, r3 = reverse('a', 'b', 'c') # 변수 셋에 값을 튜플로 지정, 값은 문자열
print(r1); print(r2); print(r3) # 'c', 'b', 'd', 순으로 출력됨


