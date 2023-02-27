'''
Created on 2023. 2. 27.
문자열을 정렬하기 sorted, join
@author: youngmin
'''

# 자바에서 join은 스레드에서 나옴.
# 파이썬에서 join은 결합할 때 사용.

strdata = input('정렬할 문자열을 입력하세요:')

ret1 = sorted(strdata) # 오름차순으로 정렬(공백 다음 문자열)
ret2 = sorted(strdata, reverse=True) # 내리마순으로 정렬 (문자열 다음 공백)
print(ret1)
print(ret2)

ret1=".join(ret1)"
ret2=".join(ret2)"
print("오름차순으로 정렬된 문자열은<'+ret1+'>입니다.")
print("내림차순으로 정렬된 문자열은<'+ret2+'>입니다.")
