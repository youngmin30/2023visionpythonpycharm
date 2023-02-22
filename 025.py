'''
Created on 2023. 2. 21.
비트 연산자 이해하기
@author: youngmin
'''


bit1 = 0x61
bit2 = 0x62

print(hex(bit1 & bit2)) # 0x60
print(hex(bit1 | bit2)) # 0x63
print(hex(bit1 ^ bit2)) # 0x3
print(hex(bit1 >> 1)) # 0x30
print(hex(bit1 << 2)) #0x184

# 비트: 1 또는 0으로 표현한다.
# 1바이트는 8비트
# 1바이트로 표현할 수 있는 수는 2의 8제곱인 256
# 문자 a, 컴퓨터는 0110 0001로 표현함
# 문자 b, 0110 0010으로 표현함