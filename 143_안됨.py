'''
Created on 2023. 3. 22.
143 read, write
바이너리 파일 복사하기
@author: youngmin
'''

bufsize = 1024 # 256*1024

f = open('img_sample.jpg', 'rb')
h = open('img_sample_copy.jpg', 'wb')

data= f.read(bufsize)

while data:
    h.write(data)
    data = f.read(bufsize)
    
f.close()
h.close()

