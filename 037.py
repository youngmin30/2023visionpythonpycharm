'''
Created on 2023. 2. 22.
036
@author: youngmin
'''

tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c'])
#tuple1[0] = 6 # 튜플은 값을 변경할 수 없음 TypeError: 'tuple' object does not support item assignment

def myfunc():
    print('안녕하세요')
    
tuple4 = (1, 2, myfunc)
tuple4[2]()