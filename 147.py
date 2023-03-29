'''
Created on 2023. 3. 22.
147
파일 삭제하기
os.remove
@author: youngmin
'''

from os import remove

target_file = 'stockcode_copy.txt'

k = input('[%s] 파일을 삭제하겠습니까? (y/n)' % target_file)

if k == 'y':
    remove(target_file)
    print('[%s]를 삭제했습니다.' % target_file)
