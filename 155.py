'''
Created on 2023. 3. 23.
155
파일이 존재하는지 체크하기
os.path.exists
@author: youngmin
'''

import os
from os.path import exists


dir_name = input('새로 생성할 디렉터리 이름을 입력하세요.:')

if not exists(dir_name): # 디렉토리에 이름이 없으면
    os.mkdir(dir_name) # 디렉토리를 만들자.
    print('[%s] 디렉터리를 생성했습니다.' % dir_name)

else:
    print('[%s]은/는 이미 존재합니다.' % dir_name)

    
    
    
    
