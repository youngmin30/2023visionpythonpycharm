'''
Created on 2023. 2. 21.
시퀀스 자료형, 연속된 자료형
@author: youngmin
'''

strdata = 'abcde' # 문자
listdata = [1, [2, 3], '안녕'] # 리스트 안에 리스트 사용 가능
tupledata = (100, 200, 300, (400, 500)) # 튜플도 튜플 안에 사용 가능

print(strdata)
print(listdata)
print(tupledata)

# 리스트와 튜플의 차이는?
# tuple, list 모두 수정 불가라고 책에 나와 있음
# tuple은 값 변경 불가한 객체
# dictionary는 키와 값의 쌍으로 되어 있고 순서는 중요하지 않다.
# 그래서 dictionary 자료형은 시퀀스가 아니다.


# key는 중복 불가
# value는 중복 불가능
dictdata = {"산대특":"비젼", "회계":"비젼", "출판":"비젼"}
print(dictdata["산대특"])


# 그건 튜플로 해야하는 것 같아. 예전에 그런 것 같아.
# (비젼, 산대특)
# (비젼, 회계)
# (비젼, 출판)


