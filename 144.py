'''
Created on 2023. 3. 22.
144
with ~ as
파일 열고 자동으로 닫기
@author: youngmin
'''

with open('stockcode.txt' 'r') as f: # with open() as f 는 파일을 연 뒤 자동으로 닫는다.
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' % (line_num+1, line), end="")
