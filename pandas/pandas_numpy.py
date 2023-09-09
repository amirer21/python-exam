import pandas as pd
import numpy as np

student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90}) #np.nan은 데이터가 없다는 의미이다.
student2 = pd.Series({'수학':80, '국어':90})

print("student1 :: ", student1)
print('\n')
print("student2 :: ", student2)
print('\n')


#데이터프레임의 연산
# +, -, *, / 연산자를 사용할 수 있다.
addition = student1 + student2               #덧셈
subtraction = student1 - student2            #뺄셈
multiplication = student1 * student2         #곱셈
division = student1 / student2               #나눗셈
print(type(division))

result = pd.DataFrame([addition, subtraction, multiplication, division], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

#add, sub, mul, div 메소드를 사용할 수 있다.
#fill_value=0 : NaN을 0으로 채운다.
sr_add = student1.add(student2, fill_value=0)    #덧셈 
sr_sub = student1.sub(student2, fill_value=0)    #뺄셈
sr_mul = student1.mul(student2, fill_value=0)    #곱셈
sr_div = student1.div(student2, fill_value=0)    #나눗셈

result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)