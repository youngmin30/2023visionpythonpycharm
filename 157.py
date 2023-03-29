'''
Created on 2023. 3. 23.
157 현재 시간을 년-월-일 시:분:초로 출력하기
localtime, strftime
@author: youngmin
'''

from time import localtime, strftime

logfile = 'test.log' # log 파일의 이름을 test.log라고 한다.

def writelog(logfile, log): # logfile, log를 매개변수로 하는 함수 writelog를 정의함.
    time_stamp = strftime('%Y-%m-%d %X\t', localtime()) # strftime()을 만듦 현재 시각을 원하는 형태로 출력
    log = time_stamp + log + '\n' # time_stamp와 log 출력하기
    
    with open(logfile, 'a', encoding="utf-8") as f: # logfile을 a로 엶.
        f.writelines(log) # 파일에 log 쓰기
        
writelog(logfile, '첫 번째로 로깅 문장입니다.')