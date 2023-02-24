'''
Created on 2023. 2. 24.
몫과 나머지 구하기 divmod
@author: youngmin
'''

a = 1000
b = 3
c = divmod(a, b) # 파이썬은 divmod(a, b) 함수 제공함. 자바는 직접 메소드 만들어 사용 가능함. 파이썬도 만들어 사용 가능함.

x, y = divmod(a, b)
print(c, x, y)
print(c)
