'''
Created on 2023. 2. 27.
문자열이 알파벳 또는 숫자인지 검사하기(isalnum)
@author: youngmin
'''


txt1 = '안녕하세요'
txt2 = '1.Title=제목을 넣으세요'
txt3 = '3피오R2D2'

ret1 = txt1.isalnum() # 변수명혹은객체명.메소드() ==> 이것은 메소드로 보자.
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()

print(ret1)
print(ret2)
print(ret3)