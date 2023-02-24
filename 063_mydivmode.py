'''
Created on 2023. 2. 24.
함수 정의
@author: youngmin
'''

# 함수 정의단
def mydivmod(a, b): # div모드가 있는 줄 모르고, 만들어 쓰게 된 경우
    m = int(a/b)
    r = a-(m*b)
    return m, r

# 실행 메소드단
if __name__ == '__main__':
    a = 1000 # 이 변수를 위 함수의 매개변수로 받는 것이므로 꼭 여기에 써야 함.
    b = 3 # 이 변수를 위 함수의 매개변수로 받는 것이므로 꼭 여기에 써야 함.
    c = divmod(a, b)
    x, y = divmod(a, b)
    print(c, x, y)
    
    c = mydivmod(a, b)
    print(c)
    
"""
python에서 제공하는 divmod() 함수, 자바에서 같은 기능의 메소드로 만들어 사용하기


1. 원본 파이썬 코드 

/* python 해당 부분
class Member(): # Member 객체에는 cnt와 name이 있음
def __init__(self, n, name): # 일반 생성자 생성 메소드, self는 자바의 this 역할
    self.cnt = n
    self.name = name
def __str__(self): # __는 자바에서는 toString()과 유사한 객체 표현 방식이다.
    #return self.name
    return f"Member(name={self.name}, cnt{self.cnt})" #f는 포맷이고 그 포맷으로 리턴하라는 의미이다.
*/


2. 파이썬 원본과 같은 기능을 자바에서 메소드로 만든 부분
package org.vision.chap15;

public class Member2py2jv {

    public static void main(String[] args) {
        // 자바는 필드 생성하고 메소드에서 필드를 가져와서 사용하지만
        // 파이썬은 필드 생성을 따로 하지 않고, 바로 사용한다.
        int cnt;
        String name;
        
        public Member2py2jv(int cnt, String name) {
            this.cnt = cnt;
            this.name = name
        }
        public String toString() {
            return "Member(name="+name+", cnt="+cnt+")";
        }

    }

}





"""