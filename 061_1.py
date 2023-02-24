'''
Created on 2023. 2. 24.
자료형 확인하기(type)
자료형에 따라 작업을 분기하여야 할 때, 자료형 확인 필요하다.
@author: youngmin
'''

numdata = 57
strdata = '파이썬'
listdata = [1, 2, 3]
dicdata ={'a':1, 'b':2}

def func():
    print('안녕하세요.')
    
print(func())
print(type(numdata)) # <class 'int'>
print(type(strdata)) # <class 'str'>
print(type(listdata)) # <class 'list'>
print(type(dicdata)) # <class 'dict'>
print(type(func)) # <class 'function'>