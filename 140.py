'''
Created on 2023. 3. 22.
write
화면에서 사용자 입력 받아 파일로 쓰기
@author: youngmin
'''

text = input('파일에 저장할 내용을 입력하세요:')

f = open('mydata.txt', 'w')

f.write(text)

f.close()