'''
Created on 2023. 2. 22.

@author: youngmin
'''

from time import sleep

for i in range(100):
    msg = '\r진행률 %d%%' %(i+1)
    print('' * len(msg), end="")
    print(msg, end="")
    sleep(0.1)