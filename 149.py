'''
Created on 2023. 3. 23.
149 
파일을 다른 디렉터리로 이동하기
os.rename
@author: youngmin
'''


from os import rename

target_file = 'stockcode.txt'
newpath = input('[%s]를 이동할 디렉터리의 절대 경로를 입력하세요:' % target_file)

if newpath[-1] == '/':
    newname = newpath + target_file
else :
    newname = newpath + '/' + target_file
    
try:
    rename(Target_file, newname)
    print(['%s] -> [%s]로 이동되었습니다.' % (target_file, newname))
except FileNotFoundError as e:
    print(e)           
    
    
