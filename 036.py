'''
Created on 2023. 2. 22.
036 리스트 이해하기 []
@author: youngmin
'''



list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c']]

list1[0] = 6
print(list1)

def myfunc():
    print('안녕하세요')
list4 = [1, 2, myfunc] # 리스트에 함수 넣음
list4[2]()
