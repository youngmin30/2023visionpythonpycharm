'''
Created on 2023. 2. 27.
정렬 연습
@author: youngmin
'''

#strdata = "가나다라차카마"

strdata = ["가", "나", "다", "라", "마", "바"]
ret = sorted(strdata); # 원본 - 정렬이 안 된 것
# print(strdata) # 가나다라차카마
# print(ret) 부분이다. # ['가', '나', '다', '라', '마', '차', '카']


# ['가', '나', '다', '라', '마', '바']
strdata.sort() # 원본을 건드리는 것
print(strdata) # 정렬된 것이 확인됨.

# ['바', '마', '라', '다', '나', '가']
ret = reversed(strdata) # 원본을 건드리지 않는다. 결과값은 한 번만 사용이 가능하다.
print(list(strdata)) # 주소가 인쇄된다면, list로 출력하면 된다.
print(list(ret))
print(list(ret)) # []
# ['바', '마', '라', '다', '나', '가']
strdata.reverse()
print(strdata)
print(list(ret)) # []