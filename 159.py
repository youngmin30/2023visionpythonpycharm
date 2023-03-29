'''
Created on 2023. 3. 24.
159 오늘의 요일 계산하기
localtime
@author: youngmin
'''

from time import localtime

weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

t = localtime()

today = '%d-%d-%d' % (t.tm_year, t.tm_mon, t.tm_mday)
week = weekdays[t.tm_wday]

print('%s 오늘은 [%s]입니다.' % (today, week))