'''
Created on 2023. 2. 27.
문자열이 숫자인지 검사하기 isdigit
@author: youngmin
'''

txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'

ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()

print(ret1) # False
print(ret2) # False
print(ret3) # True

