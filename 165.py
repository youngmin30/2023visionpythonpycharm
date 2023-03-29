'''
Created on 2023. 3. 24.
165 스택 구현하기
append, pop
@author: youngmin
'''

from hamcrest.core.core.isnone import none

mystack = [] # 빈 리스트

def putdata(data): # 함수 putdata에 파라미터로 data 넣음
    global mystack # 이 변수를 전역 변수로 사용
    mystack.append(data) # 빈 리스트에 data 넣기
    

def popdata():
    global mystack
    if len(mystack) == 0: # mystack의 길이가 0이면
        return none # 반환값 없음
    return mystack.pop() # 그렇지 않으면 mystack에 있는 것을 꺼냄.

putdata('데이터1')
putdata([3, 4, 5, 6])
putdata(12345)

print('<스택상태>:', end="");
print(mystack)

ret = popdata()
while ret != None:
    print('스택에서 데이터 추출:', end="");
    print(ret)
    print('<스택상태>:', end="");
    print(mystack)
    ret = popdata()