'''
Created on 2023. 2. 27.
리스트에서 특정 구간에 있는 요소 추출하기
@author: youngmin
'''

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

rock_planet = solarsys[1:4] # 1부터 4 앞자리인 3까지
gas_planet = solarsys[4:] # 4부터 끝까지

print('태양계의 암석형 행성:', end=""); print(rock_planet)
print("태양계의 가스형 행성:", end=""); print(gas_planet)
