'''
Created on 2023. 3. 24.
167
텍스트 파일에 있는 단어 개수 계산하기
@author: youngmin
'''

with open('mydata.txt', 'r') as f: # 파일 열기
    data = f.read() # data에 파일을 읽어서 담기
    tmp = data.split() # tmp에 data를 분리해서 넣기
    print('단어 수:[%d]' % len(tmp)) # 단어 수에 tmp 넣기
    


