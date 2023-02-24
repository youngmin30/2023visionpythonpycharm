'''
Created on 2023. 2. 23.
mylib 호출 테스트 수정(230224)
@author: youngmin
'''

from org.vision.part1.mylib import add_txt

if __name__=="__main__":
    # r = ml.add_txt('갑', '을', '병', '정', '무', '기')
    r = add_txt('갑', '을', '병', '정', '무', '기') 
    print(r)

# 모듈 가져오는 방법
# import org.vision.part1.mylib as ml 패키지에서 모듈을 가져온 것
# from.org.vision.part1 import mylib as ml 패키지에서 모듈을 가져온 것
# from org.vision.part1.mylib import add_txt 패키지 안의 모듈에서 함수를 가져온 것

