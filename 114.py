'''
Created on 2023. 2. 28.
114 리스트에 있는 요소 개수 구하기 len
@author: youngmin
'''

listdata = [2, 2, 1, 3, 8, 5, 7, 3, 6, 3, 6, 2, 3, 9, 4, 4]
listsize = len(listdata)
print(listsize) # 16

# 예상한 결과가 아님
#for num in range(100):
#        for i in listdata:
#            print(num, i)

# count()
print(listdata.count())       

# listdata에 있는 한 요소 한 요소를 1부터 순서를 매기면서 함께 출력하는 것은?
