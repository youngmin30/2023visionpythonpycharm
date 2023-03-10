'''
Created on 2023. 2. 23.
mylib 호출 테스트
@author: youngmin
'''

# import org.vision.part1.mylib as ml # 다른 패키지에 있는 모듈 가져오기
# from org.vision.part1 import mylib as ml # part1 패키지에 있는 ml을 part2에 있는 여기서 실행하기

from org.vision.part1.mylib import add_txt # 모듈뿐 아니라, 함수도 import 가능함

if __name__=="__main__":
    # r = ml.add_txt('갑', '을', '병', '정', '무', '기')
    r = add_txt('갑', '을', '병', '정', '무', '기') # mylib.py 모듈에서 정의한 add_txt 함수를 이곳에서 사용함.
    print(r)

# 모듈 가져오는 방법
# from.org.vision.part1 import mylib as ml
# 모듈에서 함수 가져오는 방법
# from org.vision.part1.mylib import add_txt
# from org.vision.part1.mylib import add_txt
