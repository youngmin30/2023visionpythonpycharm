'''
Created on 2023. 3. 24.
162 문자열의 각 문자를 그 다음 문자로 변경하기
@author: youngmin
'''

text = input('문장을 입력하세요.')

ret = ''

for i in range(len(text)): # 받은 문장의 길이를 range로 두고, 하나씩 반복
    if i != len(text)-1: # text의 길이-1이 i와 다르면
        ret += text[i+1] # text에 i+1을 더함
    else:
        ret += text[0] # text에 인덱스만큼을 더함.
    
print(ret)
