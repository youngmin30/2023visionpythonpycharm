'''
Created on 2023. 2. 28.
listPract 성티 코드
모듈명ㅇ로 숫자를 사용하지 않는다.
list 자료형의 연습: 어떤 자료형이든 CRUD 학습을 해야 한다.
create(insert)
read(select)
update(modify)
delete(remove)
@author: youngmin
'''

listData = [1, 2, 3] * 3
print(listData) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# listData.append([5, 6, 7, 8])
#listData.append(5, 6, 7, 8) # TypeError: list.append() takes exactly one argument (4 given)
#listData.append(5)
#listData.append(6)
#listData.append(7)
#listData.append(8)
#print(listData)
newlistData = [5, 6, 7, 8]
total = listData+newlistData
print(total)

# insert
listData.insert(0, 99) # isnert(위치, 값)
print(listData)

# delete
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
print(solarsys)
del solarsys[-2]
del solarsys[0]
print(solarsys)

try:
    del solarsys
    print(solarsys)
except:
    print('메모리에서 사라졌습니다.')
    
    
# crud create/insert, read/select, update/, delete/remove


