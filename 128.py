'''
Created on 2023. 3. 2.
128 사전에서 값만 추출하기 values
@author: youngmin
'''

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 
         'Bob':5887, 'Kelly':7855}

vals = names.values()
print(vals)

vals_list = list(vals)
ret = sum(vals_list)

print('출생아 수 총계: %d' % ret)