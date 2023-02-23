'''
Created on 2023. 2. 23.
함수 리턴값 이해하기
@author: youngmin
'''

def reverse(x, y, z): 
    return z, y, x


ret = reverse(1, 2, 3)
print(ret)

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1); print(r2); print(r3) # 'c', 'b', 'd', 순으로 출력됨


