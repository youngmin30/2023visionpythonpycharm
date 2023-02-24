'''
Created on 2023. 2. 24.
자료형 확인하기(type)
자료형에 따라 작업을 분기하여야 할 때, 자료형 확인 필요하다.
18세 이상, 이하 > if문이 적합
switch를 사용하려면 값이 하나여야 하므로, 범위가 답일 때에도 if문 사용
@author: youngmin
'''

# tuple
tupledata = (34, 56, 78)
print(type(tupledata)) 

def myfunc(): # myfunc() 함수 호출
    print("===")
    
print(type(myfunc)) # myfunc (당연한 얘기를 하는 것)



# intdata
intdata = 57 #"57세", 57, myfunc()일 때 모두 다름
#intData = "57세"
#intData = myfunc
print(intdata) # 57


if type(intdata) == int:
    print("자료가 정확합니다.")
elif type(intdata) == str:
    print("숫자를 입력하세요.")
else:
    print("자료가 숫자나 문자가 아닙니다.")    