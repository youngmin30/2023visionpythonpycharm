'''
Created on 2023. 2. 23.
지역 변수 전역 변수 이해하기 성티 코드
코드 확인
일단 수업 내용 그대로 커밋(책 직접 보고, 재커밋할 것)
@author: youngmin
'''

# 전역 변수: 이 모듈 전체의 영역에서 접근이 가능하다.

param = 1
strdata = '전역변수'

def func1():
    print(param, strdata) # UnboundLocalError: local variable 'param' referenced before assignment
    global param # SyntaxError: name 'param' is used prior to global declaration
    param = 2 # global
    global strdata
    strdata = '아직도 전역변수' # global
    print(param, strdata) # param과 strdata는 전역 변수
    
def func2():
    param = 2
    strdata = '지역변수'
    print(param, strdata)
    param = 999
    
# 이 모듈을 실행
if __name__ == '__main__':
    func1()
    func1()