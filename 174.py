'''
Created on 2023. 3. 27.
174 10MB 파일을 1MB 파일 10개로 분리하기
@author: youngmin
'''

filename = 'python-3.8.2.exe'
subsize = 1024 * 1024 * 3 # 3mb

suffix = 0

with open(filename, 'rb') as f:
    buf = f.read(subsize)
    while buf:
        subfilename = filename + '_' + str(suffix) # 파일 이름 뒤에 추가할 숫자를 나타냄.
        with open(subfilename, 'wb') as h:
            h.write(buf)
            print('[%s]' 완료 % subfilename)
                
        buf = f.read(subsize)
        suffix += 1