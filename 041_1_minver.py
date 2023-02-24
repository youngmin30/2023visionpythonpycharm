'''
Created on 2023. 2. 23.
지역 변수 전역 변수 이해하기 성티 코드
@author: youngmin
'''

# 전역 변수: 이 모듈 전체의 영역에서 접근이 가능하다.
param = 1
strdata = '전역변수'

def func1():
    global param # 전역변수를 전역변수 그대로 함수 안에서 사용함
    print(param, strdata) # 1 전역변수
    param = 2 # 전역변수 param을 함수 안에서 사용하면서 2 대입함
    print(param, strdata) # 2 전역변수
    
def func2():
    param = 2 # 지역 변수
    strdata = '지역변수'
    print(param, strdata) # param은 2, strdata는 지역변수
    param = 999
    print(param) # 999
    

if __name__ == '__main__': # 이 모듈을 실행
    func1() # 1 전역변수 2 전역변수
    func2() # 2 지역변수 999