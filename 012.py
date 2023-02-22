'''
Created on 2023. 2. 21.
for문 개념 배우기 for, continue, break
@author: youngmin
'''

scope = [1, 2, 3, 4, 5]

for x in scope: 
    print(x)
    if x < 3:
        continue
    else:
        break

print("=============================")

scope = [1, 2, 3, 4, 5]
for x in scope:
    print(x)
    if x >= 3:
        break