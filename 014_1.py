'''
Created on 2023. 2. 21.
014-1.py
@author: youngmin
'''

x = 1

total = 0

while 1:
    
    total = total + x
    
    if total > 10000:
        print(x) # 141
        print(total) # 10011
        break # while문에서는 반드시 break가 필요하다. 없으면 무한 루프에 빠진다.

    x = x+1
    


