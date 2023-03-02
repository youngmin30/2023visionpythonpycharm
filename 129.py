'''
Created on 2023. 3. 2.
129 사전 요소를 모두 추출하기 items 
@author: youngmin
'''

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 
         'Bob':5887, 'Kelly':7855}

items = names.items()
print(items)

for item in items :
    print(item)
