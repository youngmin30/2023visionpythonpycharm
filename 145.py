'''
Created on 2023. 3. 22.
145 seek, read, write
파일의 특정 부분만 복사하기
@author: youngmin
'''


spos = 105 # 파일을 읽는 위치 지정, 파일 최초 위치에서 105바이트 떨어진 곳
size = 500 # 읽을 크기 지정, 파일 최초 위치에서 500바이트 떨어진 곳

f = open('stockcode.txt', 'r')
h = open('stock_code.txt', 'w', encoding="utf-8")

f.seek(spos) # seek(), 파일을 읽을 위치, seek()로 spos만큼 이동
data = f.read(size) # read()
h.write(data) # wirte()

h.close()
f.close()
