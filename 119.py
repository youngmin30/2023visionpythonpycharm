'''
Created on 2023. 2. 28.
119 리스트 요소 무작위로 섞기 shuffle
@author: youngmin
'''

from random import shuffle

listdata = list(range(1, 11))

for i in range(3):
    shuffle(listdata)
    print(listdata) # 출력 결과는 실행할 때마다 달라짐
    
# [2, 1, 5, 9, 8, 7, 4, 3, 10, 6]
# [5, 8, 9, 3, 2, 7, 6, 1, 4, 10]
# [2, 6, 7, 5, 1, 9, 3, 10, 4, 8]