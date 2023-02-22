'''
Created on 2023. 2. 22.
다른 모듈의 함수를 호출해보자.
@author: youngmin
'''

# import org.vision.python.testFunction # 내가 만든 모듈 임포트
from org.vision.python.testFunction import getList
# from org.vision.python import testFunction # 모듈을 임포트하는 것
# 예) from org.vision.part2 import testfunctiona as tf
print(getList('성주원', '김덕순', '학생1', '학생2'))


