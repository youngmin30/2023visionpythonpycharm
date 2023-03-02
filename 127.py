'''
Created on 2023. 3. 2.
사전에서 키만 추출하기(keys)
@author: youngmin
'''
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 
         'Bob':5887, 'Kelly':7855}


ks = names.keys() # names 딕셔너리에서 key만 가져오기
print(ks)

for k in ks:
    print('Key %s \t Value%d' % (k, names[k]))