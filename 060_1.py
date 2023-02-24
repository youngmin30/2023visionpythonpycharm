'''
Created on 2023. 2. 24.
사용자 입력 받기(input) 성티 코드
사용자 입력시 예외 처리
@author: youngmin
'''

try: 
    ageStr = input("나이를 입력하고, 엔터 키를 누르세요.:")
    age = int(ageStr)

except: # 예외가 발생하였을 때 아래 문장 실행(오류문)
    print('나이 입력이 잘못 되었습니다.') # 세미 콜론이 있을 때나 없을 때나 실행되는데 파이썬은 세미콜론 안 씀
    ageStr = input('나이를 똑바로 입력하세요.:')
    age = int(ageStr)
    
else: # 예외가 발생하지 않았을 때 아래 문장 실행(정상적으로 등록된 경우)
    print('정상적인 나이 입력입니다. 입력한 나이는 ',age,'입니다') # 등록이 되었습니다.


    