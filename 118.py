'''
Created on 2023. 2. 28.
118 리스트 요소 정렬하기 sorted
@author: youngmin
'''

namelist = ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
ret1 = sorted(namelist)
ret2 = sorted(namelist, reverse=True)
print(namelist) # ['Mary', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
print(ret1) # ['Aimy', 'Bob', 'Kelly', 'Mary', 'Michale', 'Sams', 'Tom']
print(ret2) # ['Tom', 'Sams', 'Michale', 'Mary', 'Kelly', 'Bob', 'Aimy']

