'''
Created on 2023. 2. 27.
리스트에서 특정 요소의 위치 구하기 index
@author: youngmin
'''

solarsys = ['태양', '수성', '금성', '지구', '화성' '목성', '토성', '천왕성', '혜왕성', '지구']
planet = '지구'

pos = solarsys.index(planet) # 지구의 위치 선택
print("%s은/는 태양계에서 %d번째에 위치하고 있습니다."%(planet, pos))

post = solarsys.index(planet, 5) # 지구
print("%s은/는 태양계에서 %d번째에 위치하고 있습니다."%(planet, pos))