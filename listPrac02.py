'''
Created on 2023. 2. 28.
listPract02
@author: youngmin
'''

# 리스트의 개수가 20개 미만이면 99라는 요소로 20개를 채운다.
listData = [12, 3, 2, 43, 5, 6, 7, 4, 6, 7]
listLen = len(listData)


if listLen<20:
    for x in range(listLen, 21): # 20개이므로, 21까지
        listData.append(99) # 99를 넣음.
print(listData)

cnt = listData.count(99)
print(f'%d라는 요소가 {cnt}번 들어 있습니다.' % (99, cnt))
print(f'99라는 요소가 {cnt}번 들어 있습니다.')
print(f'%d라는 요소가 {cnt}번 들어 있습니다.' % 99)


