'''
Created on 2023. 3. 2.
123 사전에 요소 추가하기
@author: youngmin
'''

solar1 = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
solar2 = ['Sum', 'Mercury', 'Venus', 'Earth', 'Mars', 'Sturn', 'Uranus', 'Neptune']

solardict = {}

for i, k in enumerate(solar1):
    val = solar2[1] # 교재와 다른 부분
    solardict[k] = val
    
print(solardict)