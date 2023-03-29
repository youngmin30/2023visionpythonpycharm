'''
Created on 2023. 3. 22.
142 read, write
텍스트 파일 복사하기
@author: youngmin
'''

f = open('stockcode.txt', 'r')
h = open('stockcode_copy.txt', 'w', encoding='utf-8')

data = f.read()
h.write(data)
        
f.close()
h.close()
