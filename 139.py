'''
Created on 2023. 3. 22.
139 readlines
텍스트 파일을 한 줄씩 읽고 출력
@author: youngmin
'''

f = open('stockcode.txt', 'r')

lines = f.readlines()

for line_num, line in enumerate(lines):
    print('%d %s' % (line_num+1, line), end="")
    
f.close()
