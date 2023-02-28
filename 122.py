'''
Created on 2023. 2. 28.
122 리스트 요소가 모두 참인지 확인하기 all, any
@author: youngmin
'''

listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]

print(all(listdata1))
print(any(listdata2))
print(all(listdata2))
print(any(listdata2))
print(all(listdata3))
print(all(listdata3))
print(any(listdata3))
