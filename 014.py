'''
Created on 2023. 2. 21.
while문 개념 배우기(while, continue, break)
@author: youngmin
'''

x = 0

while x < 10:
    x = x+1
    # print(x)
    
    if x < 3:
        continue # while구문 처음으로 이동하여 계속 반복
    print(x)
    
    if x > 7:
        break # while 구문을 빠져 나간다.
