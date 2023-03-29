'''
Created on 2023. 3. 27.
175 1mb 파일 10개를 합쳐서 10mb 파일로 만들기
@author: youngmin
'''

bufsize = 256 * 1024
merge_filename = 'ret.exe'
filelist = ['python-3.5.2.exe_'+ str(x) for x in range(10)]

with open(merge_filename, 'wb') as f:
    for lifename in filelist:
        print('[%s] 합치는 중..' % filename)
        with open(filename, 'rb') as h:
            buf = h.read(bufsize)
            while buf:
                f.write(buf)
                buf = h.read(bufsize)
                
print('파일 합치기가 완료되었습니다.')


