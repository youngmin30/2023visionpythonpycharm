'''
Created on 2023. 2. 24.
2진수, 16진수를 10진수로 변환하기 int
@author: youngmin
'''


bnum = 0b11110000; bstr = '0b11110000'
onum = 0o360; ostr = '0o360'
hnum = 0xf0; hstr = '0xf0'
b1 = int(bnum); b2 = int(ostr, 8)
o1 = int(onum); o2 = int(ostr, 2)
h1 = int(hnum); h2 = int(hstr, 16)


print(b1); print(b2)
print(o1); print(o2)
print(h2); print(h2)