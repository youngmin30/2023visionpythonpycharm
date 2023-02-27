'''
Created on 2023. 2. 27.
리스트 요소 순서를 역순으로 만들기 reversed
@author: youngmin
'''

listdata = list(range(5)) # 0부터 4까지

ret1 = reversed(listdata) # listdata 출력하기

print('원본 리스트', end=""); print(listdata); # 원본 리스트[0, 1, 2, 3, 4]
print('역순 리스트', end=""); print(list(ret1)) # 역순 리스트[4, 3, 2, 1, 0]

ret2 = listdata[::-1]
print("슬라이싱 이용", end=""); print(ret2) # 슬라이싱 이용[4, 3, 2, 1, 0]
