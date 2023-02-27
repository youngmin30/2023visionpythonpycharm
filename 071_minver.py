'''
Created on 2023. 2. 24.
071_minver filser 많이 사용함
정수 리스트에서 소수만 걸러내기 filter
수업에서 교재 코드 다루지 않음 응용 코드 볼 것
@author: youngmin
'''

# 함수 선언
def getPrime(x): 
    if x%2 == 0: # 2로 나눈 나머지가 0이 되는, 짝수이면 x를 반환
        return # return 뒤에 반환하는 변수가 없는 것은 반환값 없이 if문 끝난다는 의미
    
    for i in range(3, int(x/2), 2): # range(start, stop, step) 3에서 시작해서, 2로 나눈 정수를 2씩 증가
        if x%i == 0: # x를 i로 나눈 나머지가 0이 되는 짝수이면 중단
            break
        
    else:
        return x # return 뒤에 반환하는 변수 x가 있는 것은 반환값 주고 else문 끝낸다는 의미
    
listdata = [117, 119, 113, 11113, 11119]
ret = filter(getPrime, listdata) # [113, 11113, 11119]
print(list(ret))
