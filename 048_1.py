'''
Created on 2023. 2. 23.
파일 열고 닫기 성티 코드
@author: youngmin
'''

# 파일 읽기1(읽고, 닫기)
f1 = open('speechText.txt', 'r', encoding='utf-8') # txt 파일의 확장자가 빠져 있으면, 읽히지 않을 수 있다.
content = f1.read()
print(content)
f1.close()


# 파일 읽기2(닫는 작업은 생략하고 읽기)
# 열었던 파일 닫는 작업 생략하는 방법
with open('speechText.txt', 'r', encoding='utf-8') as f1:
    content = f1.read()
    print(content)
