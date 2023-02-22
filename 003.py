'''
Created on 2023. 2. 20.
변수명 만들기
@author: youngmin
'''

_myname = 'youngjeon'
my_name = "영전"
MyName2 = 'Hong-gil-dong'

print(_myname)
print(my_name)
print(MyName2)



counter = 1
Counter = -2 # 자바는 변수명 앞에 _ 가능하고, #은 불가능하다.
#$Counter = -3
_Counter = -4 
print(counter)
print(Counter)
#print($Counter)
print(_Counter)


_myname = "samsjang"
my_name = "홍길동"
MyName = "유관순"
name = "김성주"


import keyword # keyWord 모듈을 가져와야 한다는 의미
print(keyword.kwlist)


# abs = 1
print(abs(-7))
