'''
Created on 2023. 3. 22.
141
텍스트 파일에 한줄씩 쓰기
writelines
@author: youngmin
'''=

count = 1
data = [] # writelines()로 읽을 때에는 list 자료형을 읽는다.
          # wirte()로 읽으려면, string 자료형을 읽는다.
print('파일에 내용을 저장하려면 내용을 입력하지 말고 [enter]를 누르세요.')

while True:
    text = input('[%d] 파일에 저장할 내용을 입력하세요: ' % count)
    
    if text == "" :
        break
    data.append(text + ' ') # 원래 코드 data.append(text + '\n')
                            # \n 대신 \s를 넣으려고 할 경우, (text + ' ')은 가능, text + '\s'는 불가능.
    count += 1
    
f = open('mydata.txt', 'w', encoding="utf-8") # encoding="utf-8"
f.writelines(data) # mydata.txt에 저장된 결과: ㄹ과 /이 한 줄씩 출력된다.
# f.write(str(data)) # mydata.txt에 저장된 결과: ['ㄹ\n', '\\\n']
# 그렇다면, 한 줄씩이 아니라 하나의 라인으로 문서 전체를 읽고 싶다면? data.strip('\n')는 불가능한데 list는 strip이 안 되기 때문에
# 리스트를 그대로 두고, text에 개행 대신 공백을 두는 것으로 수정

f.close()