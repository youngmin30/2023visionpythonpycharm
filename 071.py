'''
Created on 2023. 2. 24.
071 filser 많이 사용함
정수 리스트에서 소수만 걸러내기 filter - 교재 코드
수업에서 교재 코드 다루지 않음 응용 코드 볼 것
@author: youngmin
'''

def getPrime(x):
    if x%2 == 0:
        return 
    
    for i in range(3, int(x/2), 2):
        if x%i == 0:
            break
        
    else:
        return x
    
listdata = [117, 119, 113, 11113, 11119]
ret = filter(getPrime, listdata) # [113, 11113, 11119]
print(list(ret))
