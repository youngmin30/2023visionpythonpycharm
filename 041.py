'''
Created on 2023. 2. 23.
지역변수와 전역변수 이해하기 global - 교재 코드
041
@author: youngmin 
'''

# 전역 변수 선언(이 모듈 전체 영역에서 사용할 수 있는 변수)
param = 10
strdata = '전역변수'

# 함수 선언1
def func1():
    strdata = '지역변수' # global로 선언하지 않았으므로 지역 변수
    #print(strdata) # 지역변수

# 함수 선언2    
def func2(param): # param이라는 이름으로 사용한 매개변수일 뿐이다.
    param = 1 # 여기에서 1을 값으로 주면, 
    print(param) # 이 함수 안에서는 1을 출력하는 지역 변수로 사용된다.

# 함수 선언3    
def func3(): # 전역 변수
    global param 
    #print(param) # param = 10
    param = 50
    #print(param) # 전역 변수 param에 새 값 50 대입한 것
    
func1()
#print(strdata) # 전역 변수
#print(param) # 10

func2(param)
#print(param) # 전역변수 param인 10을 출력함. 그러나 이곳에서는 전역 변수은 10을 출력한다. 함수 안에서와 함수 밖에서 값이 다르게 출력된다.

func3()
print(param) # 50 전역 변수인 10이 아니라, func3() 함수에서 사용한 전역 변수 10을 출력한다.


# 함수2와 함수3의 차이는, global param인데
# 함수2는 함수2에서 global없이 지역변수 param을 출력하고
# 함수 밖 모듈 안에서는 전역 변수 param을 출력한다.
# 함수3은 global을 쓴 전역변수이고
# 함수 밖 모듈 안에서는 전역변수를 출력한다.
