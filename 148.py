'''
Created on 2023. 3. 22.
148
파일 이름 바꾸기
os.rename
@author: youngmin
'''

from os import rename
from win32ui import CDocTemplate_fileNewName

target_file = 'stockcode.txt'

newname = input('[%s]에 대한 새로운 파일 이름을 입력하세요:' % target_file)
rename(target_file, newname)
print('[%s] -> [%s]로 파일 이름이 변경되었습니다.' % (target_file, newname))
                
                


