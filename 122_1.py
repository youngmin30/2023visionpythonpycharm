'''
Created on 2023. 2. 28.

@author: youngmin
'''

"""
# True
# 파이썬에서는 0 이외의 숫자는 0이다.
anum = -1 # False
anum1 = 0 # False
anum2 = 1 # True
anum3 = 2
print(anum == True) # anum은 True인가, 그 결과를 내라. # False
print(anum1 == True)
print(anum2 == True)
print(anum3 == True) # False

# True ~ 1, 1.0 이외의 수는 모두 False이다.
# anum = 1.0 # 혹은 1은 True이외의 수는 모두 False이다.
print(anum == True)

listData1 = [0, 1, 2, 3, 4]
for x in listData1:
    print(x==True)
"""    


listData1 = [0, 1, 2, 3, 4]
listData2 = ["", [], (), {}, None, False, True, "1", [1]]

for x in listData2:
    print(x == True)
    
"""
, [], (), {}, None, False, True, "1", [1]

"" False 빈 문자열의 초기값
[] False 빈 리스트의 초기값
() False 빈 튜플의 초기값
{} False 빈 딕셔너리의 초기값
None False 넌의 초기값
False False 펄스의 초기값
True True 트루의 초기값
"1" False 문자 1의 초기값
[1] False 1이 담긴 리스트의 초기값
"""


listData3 = [-5, 1, 2, 3, 4]
print(all(listData3)) # [-5, 1, 2, 3, 4]

for x in listData3:
    print(x==True)
    
##################################
#while(-5):
#    print("x", end='')
##################################

