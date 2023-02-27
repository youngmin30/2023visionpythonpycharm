'''
Created on 2023. 2. 27.

@author: youngmin
'''

days = range(1, 32) # range[1, 32] 틀린 표현
print(list(days))

for x in days[::7]: # step 7
    print(x)

# 
간 = "갑을병정무기경신임계"

for x in 간:
    print(x)
    
노래 = '산토끼토끼야어디를가느냐'
ret = 노래[::-1] # reverse() 역할
print(ret) # 냐느가를디어야끼토끼토산

print(노래[::-2]) # 냐가디야토토

print(노래[-2::-2]) # 느를어끼끼산

길이 = len('당신이 입력한 문장')
print(f'당신이 입력한 문장의 길이는 {길이}입니다.')
이름 = '홍길동'
print('당신이 입력한 문장의 길이는 %d입니다.' % (이름, 길이)) # % 자리에 '%길이'를 넣으라. 결과는 같음.
print(f'당신이 입력한 문장의 길이는 {길이}입니다.') # 입력한 문장의 길이는 길이입니다.

poem = '나보기가 역겨워 가실 때에는 아름따다 가실길에 뿌리오리다.'
speech = 'government of the people'
print(len(poem), len(poem.encode())) # 15 39
# 스페이스를 한 바이트로 계산한다.
# 순수한 한글은 12자이다. 12 * 3 = 36 + 3 = 39
# 한글 한 자는 3바이트이다.(유니코드에서 그렇다.)
# 
print(len(speech), len(speech.encode())) #24 24 # len() 글자 수, 메모리 크기: len(변수명.encode())

#







    