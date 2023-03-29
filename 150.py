'''
Created on 2023. 3. 23.
150 디렉터리에 있는 파일 목록
os.listdir, glob.glob
@author: youngmin
'''

import os, glob

folder = 'd:/devlab/py200'

file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files)
print(file_list)
