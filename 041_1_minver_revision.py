'''
Created on 2023. 2. 23.
지역 변수 전역 변수 이해하기 성티 코드
041_1_minver_revision
@author: youngmin
'''

# 전역 변수: 이 모듈 전체의 영역에서 접근이 가능하다.

param = 1
strdata = '전역변수'

def func1():
    global param # 전역변수 param을 함수 안에서 그대로 쓰겠다. 
    print(param, strdata)  # 1 전역변수
      
def func2():
    param = 2
    strdata = '지역변수'
    print(param, strdata) # 2 지역변수
    param = 999
    print(param, strdata) # 999 지역변수
    

if __name__ == '__main__': # 이 모듈을 실행
    func1()
    func2()