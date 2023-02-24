'''
Created on 2023. 2. 24.
진법변환
@author: youngmin
'''

# 8진수를 10진수로
o1 = oct(100) # 스트링으로 리턴됨(8진수를 의미하는 스트링이 만들어짐)
print(o1)
res = int('0o7777', 8) # 8진수(0o로 시작함)를 10진수로 고치라.
print(res) # 4095


# 16진수
h1 = hex(97) # hex()함수는 10진수 97을 16진수(0x를 붙인다는 것)로 고치고 문자열로 표기한 것
print(h1) # 0x61
res = int(h1, 16) # 숫자로 바꾼 것
print(res)