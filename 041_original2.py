'''
Created on 2023. 2. 23.
지역변수와 전역변수 이해하기 global - original
@author: youngmin 
'''


# 전역 변수 선언
param = 1
strdata = '전역변수'

# 함수 선언
def func1():
    global param # 전역 변수를 func1()에서 그대로 사용하겠다.
    param = 2 # 전역 변수의 값을 바꾸겠다.
    global strdata # 전역 변수를 func1()에서 그대로 사용하겠다.
    strdata = '아직도 전역변수' # 전역 변수의 값을 바꾸겠다. 값이 바뀌어도 여전히 전역 변수이다.
    #print(strdata)
    
def func2(param): # 전역 변수를 func2()의 매개변수로 가져온다. 
    param = 1 # 전역 변수의 값을 바꾸겠다.
    print(param) # 결과: 1 이곳도 여전히 전역 변수이다.
    
def func3():
    global param # 전역 변수를 함수 안에서 사용하겠다.
    param = 50 # 이곳도 여전히 전역 변수이다.
    
func1()
print(strdata) # 결과: 아직도 전역변수
print(param) # 결과: 2
func2(param) 
print(param) # 결과: 2
func3()
print(param) # 결과: 50


