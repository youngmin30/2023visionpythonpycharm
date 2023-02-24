'''
Created on 2023. 2. 23.
044 파이썬 패키지 이용하기
mylibrary = 043
mylibraryTest = 044 두 코드 함께 사용
@author: youngmin
'''
# 사용 방법 성티 코드
#import mypackage.mylib
#ret1 = mypackage.mylib.add_txt('대한민국, '1등')
#ret2 = mypackage.mylib.reverse(1)

# 수정 코드
#import org.vision.part2.mylib
from org.vision.part2.mylibrary import add_txt
from org.vision.part2.mylibrary import reverse


ret1 = add_txt("대한민국", "1등")
ret2 = reverse(1)

# 이 코드를 작성하는 과정에서 알아낸 것
# from 패키지명 import 함수명


