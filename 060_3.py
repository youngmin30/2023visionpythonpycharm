'''
Created on 2023. 2. 24.
input을 통한 입력과 예외 처리2
@author: youngmin
'''

while 1:
    inputStr = input('나이를 입력하세요. ==> ')
    
    try:
        age = int(inputStr)
        pass
    except:
        print("나이 입력 오류 발생!")
        continue
        pass
    else: # 정상적인 부분
        if (age>18):
            print("입장이 가능합니다.")
        else:
            print("입장 불가")
        pass
        break; # while 루프문을 탈출한다. # break는 try문에 소속되어 있다. 
    finally:
        print("작업을 종료합니다.")
        pass