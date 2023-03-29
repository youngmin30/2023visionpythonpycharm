'''
Created on 2023. 3. 23.
151 현재 디렉터리 확인하고 바꾸기
os.getcwd, os.chdir
@author: youngmin
'''

import os

pdir = os.getcwd(); 
print(pdir) # D:\2023javaworkspace\pypart1\org\vision\part4

os.chdir('..');
print(os.getcwd()) # D:\2023javaworkspace\pypart1\org\vision

os.chdir(pdir);
print(os.getcwd()) # D:\2023javaworkspace\pypart1\org\vision\part4

