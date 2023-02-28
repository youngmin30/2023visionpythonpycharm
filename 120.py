'''
Created on 2023. 2. 28.
120 리스트의 모든 요소를 인덱스와 쌍으로 추출하기
enumerate
@author: youngmin
'''

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
ret = list(enumerate(solarsys)) # enumerate list()로 바꾸어 주어야 함.
print(ret)

for idx, value in enumerate(solarsys):
    if idx == 0: # 태양계의 1번째 천체: 수성 '1번째'로 적기 위해서 쓴 것
        continue # 태양계의 1번째 천체: 수성 '1번째'로 적기 위해서 쓴 것
    print(f'태양계의 {idx}번째 천체: {value}')

for i, body in enumerate(solarsys):
    print('태양계의 %d번째 천체: %s' %(i, body))
