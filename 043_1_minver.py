'''
Created on 2023. 2. 23.
함수 리턴값 이해하기
@author: youngmin
'''

# 함수 정의
def reverse(x, y, z, a):
    return a, z, y, x

# 함수 실행
if __name__ == '__main__':
    print(reverse(1, 2, 3, 4)) # (4, 3, 2, 1)
    ret = reverse(1, 2, 3, 4) # (4, 3, 2, 1)
    print(ret) # 4 3 2 1
    
    r1, r2, r3, r4 = reverse(1, 2, 3, 4) # 4 3 2 1
    print(r1, r2, r3, r4)
    rr1, rr2 = reverse(1, 2, 3, 4)
    print(rr1, rr2) # reverse하기로 한 대상이 4개인데, 2개만 출력하게 해서 오류 ValueError: too many values to unpack (expected 2)
    
