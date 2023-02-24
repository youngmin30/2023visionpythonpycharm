'''
Created on 2023. 2. 24.
10진수를 2진수로 변환하기 bin
@author: youngmin
'''

b1 = bin(97)
b2 = bin(98)
ret1 = b1 + b2
print(ret1) # 0b11000010b1100010

a = int(b1, 2)
b = int(b2, 2)
ret2 = a + b
print(bin(ret2)) # 0b11000011
