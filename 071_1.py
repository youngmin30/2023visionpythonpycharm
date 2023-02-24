'''
Created on 2023. 2. 24.
071 filser 많이 사용함
정수 리스트에서 소수만 걸러내기 filter 성티 코드
@author: youngmin
'''

class Member(): # Member 객체에는 cnt와 name이 있음
    def __init__(self, n, name): # 일반 생성자 생성 메소드, self는 자바의 this 역할
        self.cnt = n
        self.name = name
    def __str__(self): # __는 자바에서는 toString()과 유사한 객체 표현 방식이다.
        #return self.name
        return f"Member(name={self.name}, cnt{self.cnt})" #f는 포맷이고 그 포맷으로 리턴하라는 의미이다.
    
# filter하는 로직
def getVipList(x):
    if x.cnt>=50: # 50보다 큰 것만 걸러낸다.
        return x # 필터에서 선택 받게 하는 것
    
if __name__ == '__main__':
    listMem = [Member(100, '윤선도'), Member(37, '홍어'), Member(28, '문어'), Member(57, '명구')]
    ret = filter(getVipList, listMem) #vip 우수고객
    #print(listMem(ret))
    #print(list(ret.__srt__()))
    #print(list(ret))
    
    # 거르는 로직
    ret = filter(getVipList, listMem)
    for r in list(ret):
        print(r)

