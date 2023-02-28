'''
Created on 2023. 2. 28.
109 append
@author: youngmin
'''

# 객체.append() ==> append는 메소드

listdata = []
# 세 번 입력할 수 있도록 한 것
for i in range(3):
    txt = input('리스트에 추가할 값을 입력하세요[%d/3]:' % (i+1)) # 총 페이지 중 현재 페이지로 응용할 수 있음
    listdata.append(txt)
    print(listdata)