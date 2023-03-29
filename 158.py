'''
Created on 2023. 3. 24.
158 올해 경과된 날짜 수 계산하기
localtime
@author: youngmin
'''

from time import localtime # localtime 모듈 사용

t = localtime() # t에 localtime() 함수 저장

start_day = '%d-01-01' % t.tm_year # t에서 나온 tm_year 메소드로 나온 값을 해당 형식에 맞게 출력
elapsed_day = t.tm_yday # 위와 동일

print('오늘은 [%s] 이후 [%d]일째 되는 날입니다.' % (start_day, elapsed_day))


