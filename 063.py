'''
Created on 2023. 2. 24.
몫과 나머지 구하기 divmod
@author: youngmin
'''

a = 11113
b = 23
ret1, ret2 = divmod(a, b)
print('<%d/ %d>는 몫이 <%d>, 나머지가 <%d>입니다.' % (a, b, ret1, ret2))
