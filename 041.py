'''
Created on 2023. 2. 23.
지역변수와 전역변수 이해하기 global
@author: youngmin 
'''


param = 10 
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print(strdata)
    
def func2(param):
    param = 1
    print(param)
    
def func3():
    global param
    param = 50
    
func1()
print(strdata)
print(param)
func2(param) 
print(param) 
func3()
print(param)


