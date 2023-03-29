'''
Created on 2023. 3. 27.
178 zip 파일 압축 풀기
@author: youngmin
'''

from zipfile import *

def extractZip(zipname):
    with ZipFile(zipname, 'r') as ziph:
        ziph.extractall()
        print('[%s]가 성공적으로 추출되었습니다.' % zipname)
        
extraZip('files.zip')


