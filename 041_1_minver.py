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
    global param # SyntaxError: name 'param' is used prior to global declaration
    # param은 global을 미리 선언하면, 지역 변수로 사용되는데, strdata는 global을 사용해도 여전히 전역 변수로 보임
    print(param, strdata) # param 1 strdata 전역변수 # UnboundLocalError: local variable 'param' referenced before assignment
    param = 2 # global 
    #global strdata # SyntaxError: name 'strdata' is used prior to global declaration
    #strdata = '아직도 전역변수' # global
    print(param, strdata) # param은 1, strdata는 전역변수 # param과 strdata는 전역 변수
    # global: 함수 안에서 전역 변수를 쓰려면, param 앞에 global을 쓴다. param 외의 다른 변수는 global과 쓰지 않는 것으로 보인다.
    # param: 함수 안에서 전역 변수를 전역 변수로 사용하고 싶을 때, global 뒤에 변수로 쓴다.
    
def func2():
    param = 2 # 지역 변수
    strdata = '지역변수'
    print(param, strdata) # param은 2, strdata는 지역변수
    param = 999
    print(param) # 지역 변수 안에서는 값을 자유롭게 바꿀 수 있다.
    # 전역 변수로 미리 선언된 변수도, 지역 변수로 새로 값을 넣어서 쓸 수 있다.
    
# 이 모듈을 실행
if __name__ == '__main__':
    func1() # 1 전역변수 2 전역변수
    func1() # 2 전역변수 2 전역변수 ==> 같은 func1인데, 다른 결과가 나옴
    func2() # 2 지역변수 999