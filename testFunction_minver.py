'''
Created on 2023. 2. 22.
함수 인자 이해하기
@author: youngmin
'''

def add(t1, t2):
    # 자료형 확인 방법1 
    # pass
    # 틀린 줄 if type(t1) == "<class 'int'>": # type(s)란 type(t1)를 의미한다.== unsupported operand type(s) for +: 'int' and 'str' ==를 지원하지 않는다는 의미이다.
    if isinstance(t1, int): # t1의 타입을 물을 때, isinstance()를 사용함.
        return (t1+t2)
    else :
        return (t1+","+t2)
    
    
    
# 함수의 값
def sum(a=100, b=200): # 디폴트 값으로, 정한 것이 아래에서 출력됨
    return a+b;
    

# 함수의 합
def hab(*nums): # * 하나 붙은 것은 자바에서 가변형 인수와 같다.
    print(nums) # 가변형 인수들이 튜플에 저장된다. 튜플은 시퀀스이므로, for 문장에서 쓸 수 있다.
    total = 0 # None이 아니라, 0
    for x in nums: # 여기에서 튜플을 사용할 수 있다.
        total = total + x
    return total
    

# 함수 리스트 조작
def getList(*names):
    nameList = [] # 리스트를 만들어서 리턴한다.
    for x in names:
        nameList.append(x)
    return nameList


# 가로, 세로에 변수를 주고, **kargs는 가변형 인수이다. 값을 넣고, 딕셔너리형으로 바꿔 준다.
# 
def somefunc(galo, selo, **kargs):
    print(kargs) # 딕셔너리로 바꿔 준다.


# 자바의 메인 메소드와 같은 부분(파이썬에서는 모듈, 자바의 클래스와 같지 않고, 이 파이썬 모듈에는 클래스가 없다. 다만, 메인이 전체를 제어한다는 것은 유사하
if __name__ == "__main__": # 공식과 같이 알아두라.

# 메인 메소드 블록을 추가하면서, 이 부분을 모두 들여씀.
    # print(type(123)) # <class 'int'>
    print(add(10, 20))
    print(add("김국진", "윤소라"))
    print(type(123)) # 자료형 확인 방법2
    
    # 함수의 값
    print(sum()) # 300
    print(sum(10)) # 210 ==> a가 10으로 바뀌었기 때문에 210이 된다. 디폴트는 100이지만, 여기에서 10을 준 것
    print(sum(b=20)) # 120 ==> b를 20으로 지정했으므로, 300이 된다. 디폴트는 200이지만.
    print(sum(45, 45)) # a, b 모두를 새로 지정할 수 있다.
    print(sum(b=1000, a=2000))
    
    
    # 함수의 합, 가변형 인수
    print(hab(1, 2, 3, 4, 5, 6, 7, 8)) # 매개변수를 자유롭게 넣을 수 있다.
    print(hab()) # 0
    
    
    # 
    print(getList('성삼문','박팽년','하위지','유응부')) # ['성삼문', '박팽년', '하위지', '유응부']
    
    #
    somefunc(10, 20, 높이=78, 밑변=65) # {'높이': 78, '밑변': 65}










