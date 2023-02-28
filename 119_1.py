'''
Created on 2023. 2. 28.
트럼프 흉내내기
트럼프 카드 게임 만들기
@author: youngmin
'''

tlist = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'Queen', 'King'] # 13
tpair = ['◆', '♣', '♠', '♥'] # 다이아몬드, 클로버, 스페이드, 하트 # 14
trump = []

# print(len(tlist)) tlist에 있는 항목의 수
# print(trump) trump에서 나올 수 있는 수

for x in tlist: # tlist의 요소를 x에 넣는다.
    for y in tpair: # tpair의 요소를 y에 넣는다.
        trump.append((x, y)) # x와 y를 trump에 넣는다.
        
trump.append(('black', 'jocker')) # 조커1
trump.append(('color', 'jocker')) # 조커2 총 54장의 조합
print(len(trump)) # 52

# 패를 섞는다.
from random import shuffle
shuffle(trump)
print(trump)


# 카드 54개: 13 * 4 = 52개, 조커 두 장


# 사람들에게 나눠주기
print(trump[0:10]) # print(trump[0, 10])이 아니라, [0:10]
print(trump[10:20])
print(trump[20:30])
