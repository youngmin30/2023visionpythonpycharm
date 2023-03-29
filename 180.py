'''
Created on 2023. 3. 27.
180 남녀 파트너 정해주기 프로그램 만들기 zip
@author: youngmin
'''

from random import shuffle

male = ['슈퍼맨', '심봉사', '로미오', '이몽룡', '마루치']
female = ['원더우먼', '뺑덕', '줄리엣', '성춘향', '아라치']

shuffle(male)
shuffle(female)

couples = zip(male, female) # zip으로 섞은 것을 묶음.

for i, couple in enumerate(couples): # enumerate는 파이썬 내장 함수
    print('커플 %d: [%s]-[%s]' % (i+1, couple[0], couple[1]))