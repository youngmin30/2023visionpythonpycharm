'''
Created on 2023. 2. 28.
리스트 정렬하기
@author: youngmin
'''

names = ['이재명', '정청래', '홍준표', '한동훈', '나경원']
# 원본에 영향없이 새로운 자료로 정렬하기

ret = sorted(names) # ret = sorted(names)
print(f'원본:{names}') # ret는 원본이 아니고, names가 원본임.
print(f'새 데이터:{ret})')

ret2 = reversed(ret)
print(f'새 데이터:{list(ret2)}')

######################################################
nameList = ['유아인', '유승준', '소희', '김만배', '젤렌스키', '위도도']
