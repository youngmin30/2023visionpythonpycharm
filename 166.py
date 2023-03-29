'''
Created on 2023. 3. 24.
166
문장에 나타나는 문자 빈도 수 계산하기
@author: youngmin
'''
from astropy.units import fa, farad

def getTextFreq(filename):
    with open(filename, 'r') as f:
        
        text = f.read()
        fa = {}
        for c in text:
            if c in fa:
                fa[c] += 1
            else:
                fa[c] = 1
                
        return fa
    
ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key = lambda x:x[1], reverse = True)
for c, freq in ret:
    if c == '\n':
        continue
    print('[%c]->[%d]회 나타남' % (c, freq))
           
