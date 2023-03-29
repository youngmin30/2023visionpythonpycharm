'''
Created on 2023. 3. 22.
146
파일 크기 구하기
os.path.getsize
@author: youngmin
'''

from os.path import getsize

file1 = 'stockcode.txt'
file2 = 'D:\2023javaworkspace\pypart1\org\vision\part4.img_saple.jpg'

file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name: %s\File Size: %d' %(file1, file_size1))
print('File Name: %s\tFile Size: %d' %(file2, file_size2))
