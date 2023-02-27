'''
Created on 2023. 2. 24.
071_1_minver filser 많이 사용함
정수 리스트에서 소수만 걸러내기 filter 성티 코드

__init__로 생성한 객체들을 ListMem이라는 리스트에 담은 뒤에
그 리스트에서 조건에 맞는(cnt가 50 이상인) 객체들을 출력할 때,
출력 양식에 포맷팅을 사용한 예제

@author: youngmin
'''

# 클래스 선언, 클래스 안에 둘 이상의 함수 선언
class Member(): # Member 객체에는 cnt와 name이 있음
    # __init__는 일반 생성자 생성 메소드, self는 자바의 this 역할
    def __init__(self, n, name):
        self.cnt = n
        self.name = name
    # __str__는 자바에서는 toString()과 유사한 객체 표현 방식이다.
    def __str__(self):
        # return self.name
        return f"Member(name={self.name}, cnt{self.cnt})" #f는 포맷이고 그 포맷으로 리턴하라는 의미이다.
"""
        f"Member(name={self.name}, cnt{self.cnt})는 포맷팅하는 것
        %d에 정수를 포맷팅해서 출력하는 기초 예제와 같이
        f"Member(name=, cnt,)"라는 구조에 {self.name}, {self.cnt} 값을 받아서 포맷팅하겠다는 의미
        실행 결과는 아래와 같은데,
        Member(name=윤선도, cnt100)
        Member(name=명구, cnt57)
        위 실행 결과와 같이 아래 listMem에서 고객 점수 cnt가 50 이상인 윤선도와 명구가
        {self.name} 자리에 포맷팅되어 출력됨.
        {self.cnt}에도 윤선도와 명구의 cnt가 포맷팅되어 출력된 것 
        
"""        
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
    ret = filter(getVipList, listMem) # filter(함수명, 함수 안 객체가 담긴 리스트)
    for r in list(ret):
        print(r)


"""
listMem = [Member(100, '윤선도'), Member(37, '홍어'), Member(28, '문어'), Member(57, '명구')]

listMem이라는 리스트 안에 Member(100, '윤선도')라는 항목의 객체가 만들어진 것.
이 객체는 튜플이나 리스트, 스트링 등 어떤 특정 자료형이 아니라 위에서 __init__로 생성된 객체이다.

"""