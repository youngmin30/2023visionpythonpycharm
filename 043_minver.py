'''
Created on 2023. 2. 23.
파이썬 모듈 이해하기
@author: youngmin
'''

# 모듈 가져오기
import time

print('5초간 프로그램을 정지합니다.') # 이용자가 확인할 메시지
time.sleep(5) # time에 있는 sleep(시간) 함수 일종의 메소드 사용
print('5초가 지나갔습니다.') # 이용자가 확인할 메시지

# 자바와의 차이: thread.sleep()은 예외 처리가 필요함.

