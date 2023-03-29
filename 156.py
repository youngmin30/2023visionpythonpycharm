'''
Created on 2023. 3. 23.
156 파일인지 디렉토리인지 확인하기

os.path.isfile
os.path.isdir
@author: youngmin
'''

import os
from os.path import exists, isdir, isfile

files = os.listdir()
for file in files:
    if isdir(file):
        print('DIR: %s' % file)
        
for file in files:
    if isfile(file):
        print('FILEl %s' % file)

