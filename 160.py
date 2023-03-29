'''
Created on 2023. 3. 24.
160 프로그램 실행 시간 계산하기
datetime.now
@author: youngmin
'''

from datetime import datetime
from navigator_updater.app import start

start = datetime.now() # datetime.now() 현재 시각을 시작 시간으로 함

print('1에서 백만까지 더합니다.')

ret = 0
for i in range(1000001): # range는 1000000까지이므로 1을 더한 것을 넣음.
    ret += i # ret = ret + i
print('1에서 백만까지 더한 결과: %d' % ret) # 1부터 백만까지를 모두 더한 값을 %d에 넣음

end = datetime.now() # 프로그램이 끝난 시간을 end 객체로 만듦.
elapsed = end - start # end에서 start 시간을 빼고, elapsed에 넣음.
print('총 계산 시간:', end="");
print(elapsed)

elapsed_ms = int(elapsed.total_seconds() * 100)
print('총 계산 시간: % dms' % elapsed_ms)