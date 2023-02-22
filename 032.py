'''
Created on 2023. 2. 21.
멤버 체크 이해하기(in)
@author: youngmin
'''


listdata = [1, 2, 3, 4]
ret1 = 5 in listdata # False 없으니까 false
ret2 = 4 in listdata # True 있으니까 4
print(ret1); print(ret2)

strdata = 'abcde'
ret3 = 'c' in strdata # True
ret4 = '1' in strdata # False
print(ret3); print(ret4)



