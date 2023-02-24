'''
Created on 2023. 2. 23.
041_original
지역변수와 전역변수 이해하기 global - original2
@author: youngmin 
'''


# 전역 변수: 이 모듈 전체에서 접근할 수 있는 변수
param = 100
strdata = '전역변수'

def func1():
    global param
    param = 2 # 전역변수의 값을 새로이 함
    global strdata
    strdata = '아직도 전역변수' # 전역변수의 값을 새로이 함.
    print(param, strdata) # 2 아직도 전역변수

def func2():
    strdata = '지역변수' # global 선언이 없어서 지역변수
    param = 999
    print(param, strdata) # 999 지역변수
    
# 이 모듈을 실행
if __name__ == '__main__':
    func1()
    func2()

