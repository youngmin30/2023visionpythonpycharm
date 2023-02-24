'''
Created on 2023. 2. 24.
10진수를 16진수로 변환하기 hex
@author: youngmin
'''

h1 = hex(97)
h2 = hex(98)
ret1 = h1 + h2
print(ret1) # 0x610x62

a = int(h1, 16)
b = int(h2, 16)
ret2 = a + b
print(hex(ret2)) # 0xc3