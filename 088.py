'''
Created on 2023. 2. 27.
공백 lstrip(), rstrip(), strip()
@author: youngmin
'''

txt = ' 양쪽에 공백이 있는 문자열입니다. '
print(txt)

txt1 = ' 왼쪽에 공백이 없는 문자열입니다. '
ret1 = txt1.lstrip()
print(ret1)

txt2 = ' 오른쪽에 공백이 없는 문자열입니다. '
ret2 = txt2.rstrip()
print(ret2)

txt2 = ' 양쪽에 공백이 없는 문자열입니다. '
ret3 = txt.strip()
print(ret3)