'''
Created on 2023. 2. 20.
자료형 개념 배우기
@author: youngmin
'''

int_data = 135;
float_data = 3.141592;
complex_data = 1+5j; # 복소수
str_1 = "Ich labe dich.";
str_2 = "Ich 'labe' dich";

print(str_1, str_2)

list_data = [1, 2, 3, 4, 5, "갑", '을'] # 파이썬은 무조건 대괄호를 열고 닫음

list_data = [1, 2, 3, "갑", "을"]; list_data[4] = '병'
tuple_data = (1, 2, 3, "갑", "을"); # tuple_data[4] = '병' # runtime exception
print(list_data, tuple_data)

dict_data = {'홍길동': 70, '윤선도':100, '안중근':100}

# 윤선도의 점수를 조회하고, 색인하고 싶은 경우
print('윤선도 점수:', dict_data['윤선도'])


##########################################
# 딕셔너리 데이터를 이터러블하게(반복) 처리하는 예제

dic_it = iter(dict_data) # dict_data를 반복하는 함수


for x in dic_it: # for(String x:dict_it){}
    print(x, dict_data[x])
    






