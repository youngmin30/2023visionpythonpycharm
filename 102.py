'''
Created on 2023. 2. 27.
리스트에서 특정 위치의 요소를 변경하기
@author: youngmin
'''

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

planet = '화성'

pos = solarsys.index(planet) # planet은 '화성'이고', '화성' 자리에 Mars를 넣은 것
solarsys [pos] = 'Mars' # index(planet)을 [pos]라고 두고, '화성'을 'Mars'로 변경
print(solarsys)