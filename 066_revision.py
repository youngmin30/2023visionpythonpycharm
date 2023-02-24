'''
Created on 2023. 2. 24.
066 2진수, 16진수를 10진수로 변환하기 int
@author: youngmin
'''

"""
bnum = 0b11110000; bstr = '0b11110000' # 0b 2진수 바이너리 넘버 2진수
onum = 0o360; ostr = '0o360' #0o 8진수
hnum = 0x0; hstr = '0xf0' #0x 16진수


b1 = int(bnum); b2 = int(ostr, 2)
o1 = int(onum); o2 = int(ostr, 8) # ValueError: invalid literal for int() with base 2: '0o360'
h1 = int(hnum); h2 = int(hstr, 16)


print(b1); print(b2)
print(o1); print(o2)
print(h2); print(h2)
"""


################ 다시 확인 ############################# 진수를 숫자로
bnum = 0b11110000; # 0b 2진수 바이너리 넘버 2진수
onum = 0o360; #0o 8진수
hnum = 0x0; #0x 16진수

print(type(bnum)) # <class 'int'> 타입만 확인
print(bnum) # 240
print(onum) # 240
print(hnum) # 0

############################# 진수를 스트링으로
bstr = '0b11110000' # 0b 2진수 바이너리 넘버 2진수
ostr = '0o360' #0o 8진수
hstr = '0xf0' #0x 16진수

print(bstr) # 240
print(ostr) # 240
print(hstr) # 0

#############################

# b2 = int(ostr, 2) # ValueError: invalid literal for int() with base 2: '0o360'
o2 = int(ostr, 8) # ValueError: invalid literal for int() with base 2: '0o360'
h2 = int(hstr, 16)

# print(b2)
print(o2)
print(h2)
#############################



