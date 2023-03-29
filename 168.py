'''
Created on 2023. 3. 24.
168 파일에서 특정 단어 개수 계산하기
@author: youngmin
'''

def countWord(filename, word): # 파일 이름, 단어를 매개 변수로 한 함수 countWord() 열기
    with open(filename, 'r') as f: # 파일, 읽기 모드로 열기
        text = f.read() # 파일 읽어서 text에 담기
        text = text.lower() # 파일 읽어서 text에 담기, 소문자로 쓰기
        pos = text.find(word) # 파일 읽어서 word에 담기
        count = 0 # count에 0 입력하기
        
        while pos != -1: # pos에 -1 입력하기
            count += 1 # count는 0인데, post가 -1이 아닌 때, 1씩 증가시키기
            pos = text.find(word, pos+1) # text에 word와 pos+1 입력하기
        return count

word = input('mydata.txt에서 개수를 구할 단어를 입력하세요.')
word = word.lower() # word를 소문자로 줄이기
ret = countWord('mydata.txt', word) # 텍스트에서 word 찾기
print('%s의 개수: %d % (word, ret)') # %s의 개수에 word와 ret 입력하기
       