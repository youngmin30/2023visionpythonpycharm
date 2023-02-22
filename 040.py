'''
Created on 2023. 2. 22.
040 함수 인자 이해하기
@author: youngmin
'''

def add_txt(t1, t2='파이썬'):
    print(t1+':'+t2) # 베스트:파이썬
    
add_txt('베스트') 
add_txt(t2='대한민국', t1='1등') # 1등:대한민국

def func1(*args): # () *args 가변형 인수
    print(args)
    
def func2(width, height, **kwargs): # (3, 5, 1, 5) **kwargs 딕셔너리형으로 넣으라
    print(kwargs) # {}

func1()
func1(3, 5, 1, 5)
func2(10, 20) # **kwargs 이 부분은 인수가 부족한 때는 생략 가능하다. 
func2(10, 20, depth=50, color='blue') # {'depth': 50, 'color': 'blue'}