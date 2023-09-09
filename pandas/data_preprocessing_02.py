#데이터 전처리란 데이터를 분석하기 좋은 형태로 만들어 주는 것을 말한다.
#영어로는 Data Preprocessing이라고 한다.

#데이터 전처리는 데이터 분석의 성능을 향상시키는데 중요한 역할을 한다.
#데이터 전처리를 하지 않으면 데이터 분석의 결과가 잘 나오지 않을 뿐만 아니라
#잘못된 결과를 도출할 수도 있다.

# 순서
# 1 누락 데이터 처리
# 2 중복 데이터 처리
# 3 데이터 표준화
# 4 데이터 범주화(카테고리) 처리
# 5 데이터 정규화
# 6 시계열 데이터 처리


###########
# 2 중복 데이터 처리
import pandas as pd

df = pd.DataFrame({'c1':['a','a','b','a','b'],
                     'c2':[1,1,1,2,2],
                     'c3':[1,1,2,2,2]})
print(df)
print("\n")
print("=========================================")
'''
  c1  c2  c3
0  a   1   1
1  a   1   1
2  b   1   2
3  a   2   2
4  b   2   2
'''

#전체 행 데이터 중에서 중복값 찾기
df_dup = df.duplicated() #duplicated() : 데이터의 중복 여부를 True, False로 반환한다.
print(df_dup)  
print("\n")
print("=========================================")
'''
0    False
1     True
2    False
3    False
4    False
dtype: bool
'''

#특정 열 데이터에서 중복값 찾기
col_dup = df['c2'].duplicated() #duplicated() : 데이터의 중복 여부를 True, False로 반환한다.
print(col_dup)
print("\n")
print("=========================================")
'''
0    False
1     True
2     True
3    False
4     True
Name: c2, dtype: bool
'''


#중복된 행 제거
df2 = df.drop_duplicates() #drop_duplicates() : 중복된 행을 제거한다.
print(df2)
print("\n")
print("=========================================")
'''
  c1  c2  c3
0  a   1   1
2  b   1   2
3  a   2   2
4  b   2   2
'''

#c2, c3열을 기준으로 중복된 행 제거
# c2, c3열의 값을 기준으로 중복값이 있는 행을 제거한다.
df3 = df.drop_duplicates(subset=['c2','c3']) #drop_duplicates() : 중복된 행을 제거한다.
print(df3)
print("\n")
print("=========================================")
'''
  c1  c2  c3   
0  a   1  1
2  b   1  2
3  a   2  2
'''
