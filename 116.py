'''
Created on 2023. 2. 28.
116 리스트 제거하기 del
@author: youngmin
'''

listdata = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
del listdata # 메모리에서 제거
print(listdata) # 메모리에서 제거되었으므로 오류 발생 NameError: name 'listdata' is not defined
