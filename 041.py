'''
Created on 2023. 2. 23.
지역변수와 전역변수 이해하기 global
@author: youngmin 
'''


param = 10 # 이 파람과 아래 파람은 다른 파람이다.(imo; 이 모듈의 전역변수 파람)
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    #print(strdata) # 지역변수 ==> 함수 안에서는 지역변수, 전역변수 아님.
    
def func2(param): # 이 파람과 위 파람은 다른 파람이다. (imo; func2의 지역변수 파람) 
    param = 1
    print(param) # 1 def2의 param은 지역변수인 1이다.
    
def func3():
    global param
    param = 50
    
func1() # 지역 변수 출력
print(strdata) # 전역변수
print(param) # 10
func2(param) 
print(param) # 10 이 모듈의 param은 전역변수인 10이다.
func3()
print(param) # 50이 출력됨


