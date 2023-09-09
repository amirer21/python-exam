import pandas as pd

#pandas는 데이터 분석을 위한 파이썬 라이브러리이다.
#pandas는 행과 열로 이루어진 2차원 데이터프레임을 만들어 다룰 수 있다.
#pandas는 다음과 같은 기능을 제공한다.
#1. 데이터 핸들링
#2. 결측치 처리
#3. 데이터 정렬
#4. 데이터 요약
#5. 데이터 병합
#6. 데이터 변환
#7. 데이터 시각화

#pandas의 자료구조
#1. 시리즈(Series) : 1차원 배열
#2. 데이터프레임(DataFrame) : 2차원 배열
#3. 패널(Panel) : 3차원 배열

# import pandas as pd #pandas 라이브러리를 불러온다.

# 1. 시리즈(series)
# pandas의 시리즈는 1차원 배열이다. series는 index와 value로 구성된다. series는 index를 지정하지 않으면 0부터 시작하는 정수형 인덱스를 사용한다.
#ser
# 1-1. series
dict_data = {'name': ['A', 'B', 'C', 'D'],
        'score': [100, 90, 80, 70],
        'grade': ['A', 'B', 'C', 'D']}
# dictionary -> series 타입으로 변환
print(type(dict_data)) #<class 'dict'>
# 형태 : pandas.Series(딕셔너리)
df = pd.Series(dict_data)
print(type(df)) #<class 'pandas.core.series.Series'>
print(df)
"""
출력 결과 : 키와 값이 출력된다.
name          [A, B, C, D]
score    [100, 90, 80, 70]
grade         [A, B, C, D]
"""
        
# 1-2. series index
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)
"""
출력 결과 : 인덱스가 자동으로 생성된다.
0    2019-01-02
1          3.14
2           ABC
3           100
4          True
"""
idx = sr.index
val = sr.values
print(idx)
print(val)


# 1-3. series element
#tuple -> series 타입으로 변환
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

#원소 1개 선택
print(sr[0])
print(sr['이름'])

#원소 여러 개 선택
print(sr[[1,2]])
print(sr[['생년월일', '성별']])

#원소 범위 선택
print(sr[1:2])
print(sr['생년월일':'성별'])


# 2. 데이터프레임(DataFrame)

# DataFrame은 2차원 배열이다. DataFrame은 행과 열로 이루어진 2차원 배열이다. DataFrame은 index와 column으로 구성된다. DataFrame은 index를 지정하지 않으면 0부터 시작하는 정수형 인덱스를 사용한다.
# 

# 2-1. DataFrame
# 데이터 프레임 변환 형식 : pandas.DataFrame(딕셔너리)
# dict -> dataframe 타입으로 변환
dict_data = {'c0': [1,2,3], 'c1': [4,5,6], 'c2': [7,8,9], 'c3': [10,11,12], 'c4': [13,14,15]}
df = pd.DataFrame(dict_data)
print(type(df)) #<class 'pandas.core.frame.DataFrame'>
print(df)
"""
   c0  c1  c2  c3  c4
0   1   4   7  10  13
1   2   5   8  11  14
2   3   6   9  12  15
"""
print(df.index) #행
print(df.columns) #열
#행(index), 열 이름 변경
df.index = ['r0', 'r1', 'r2']
df.columns = ['a', 'b', 'c', 'd', 'e']
print(df)
"""
    a  b  c   d   e
r0  1  4  7  10  13
r1  2  5  8  11  14
r2  3  6  9  12  15
"""
df.rename(columns={'a': 'c0', 'b': 'c1', 'c': 'c2', 'd': 'c3', 'e': 'c4'}, inplace=True)
df.rename(index={'r0': 'r00', 'r1': 'r11', 'r2': 'r22'}, inplace=True)
print(df)
#df memory address
print(id(df)) #1661031989056

#inplace=True : 원본 객체를 변경한다.
#inplace=False : 원본 객체를 변경하지 않고, 변경된 결과를 새로운 객체에 저장한다.
tmp_df = df.rename(columns={'c0': 'a', 'c1': 'b', 'c2': 'c', 'c3': 'd', 'c4': 'e'}, inplace=False)
tmp_df = df.rename(index={'r00': 'r0', 'r11': 'r1', 'r22': 'r2'}, inplace=False)
print(tmp_df)
print(id(tmp_df)) #1661031988912

def rename(colums, inplace):
    if inplace:
        df.columns = colums
    else:
        tmp_df = df[:] #원본 복사하여 새로운 공간에 저장
        tmp_df.columns = colums
        return tmp_df
    
#data remove
tmp_df1 = df[:]
print("remove before :: ", tmp_df1)
"""
     c0  c1  c2  c3  c4
r00   1   4   7  10  13
r11   2   5   8  11  14
r22   3   6   9  12  15
"""
tmp_df1.drop('r00', inplace=True)
print("index remove after :: ", tmp_df1)
#행(index)에서 r00 삭제
"""
     c0  c1  c2  c3  c4
r11   2   5   8  11  14
r22   3   6   9  12  15
"""

tmp_df2 = df[:]
tmp_df2.drop(['r11', 'r22'], axis=0, inplace=True)
print("index remove after :: ", tmp_df2)

#drop column   
tmp_df3 = df[:]
tmp_df3.drop('c0', axis=1, inplace=True)
print("column remove after :: ", tmp_df3)


#2023.09.06
'''
행(인덱스), 열 이름 설정 방법
loc, iloc 사용하여 행 선택 방법
행과 열 선택 방법
범위 슬라이싱을 사용하여 행 선택 방법
행(인덱스), 열로 바꾸는 방법
행, 열의 위치 바꾸는 방법
행, 열 추가 방법
덧셈, 뺄셈, 곱셈, 나눗셈 연산 방법
'''



dict_data = {'국어': [90, 95, 80, 85], '영어': [85, 90, 85, 90], '수학': [80, 85, 90, 95]}
df = pd.DataFrame(dict_data)
df.index = ['길동', '영희', '철수', '영수'] #행 인덱스 설정
df.columns = ['국어', '영어', '수학'] # 열 이름 설정
print(df)
"""
출력 내용
     국어  영어  수학
길동  90  85  80
영희  95  90  85
철수  80  85  90
영수  85  90  95
"""

# (조회,선택하기) loc, iloc 사용하여 행 선택하기
#인덱스 이름 : DataFrame 객체.loc[행 인덱스, 열 이름]
# 예 : df.loc['길동', '국어']
#정수 위치 인덱스 : DataFrame 객체.iloc[행 번호, 열 번호]
# 예 : df.iloc[0, 0]

# 행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['길동', '영희']]
position2 = df.iloc[[0, 1]]
print("label2 :: ", label2)
print('\n')
print(position2)
print('\n')

# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['길동':'영희']
position3 = df.iloc[0:1]
print("label3 :: ", label3)
print('\n')
print(position3)

#2개 이상 원소 출력
label4 = df.loc['길동', ['국어', '영어']]
print("label4 :: ", label4)
"""
국어    90
영어    85
"""
d = df.iloc[0, [0, 1]]
print("d :: ", d)
"""
국어    90
영어    85
"""

math1 = df['수학']
print("수학 :: ", math1)
print(type(math1))
print('\n')
'''
수학 ::  
길동    80
영희    85
철수    90
영수    95
'''


english = df['영어']
print("영어 :: ", english)
'''
영어 ::  
길동    85
영희    90
철수    85
영수    90
'''
print(type(english))
print('\n')

music_gym = df[['국어', '영어']]
print(music_gym)
print(type(music_gym))
print('\n')

math2 = df[['수학']]
print(math2)
print(type(math2))



#set_index는 행 인덱스를 열로 바꾼다.
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
print(df)
print('\n')

g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
h = df.iloc[[0, 1], [2, 3]] 
print(h)

"""
출력 내용
    음악   체육
이름
서준  85  100
우현  95   90
"""

## 행 추가하기

df['국어'] = 80 #모든 컬럼의 값을 80으로 변경
print(df)

#새로운 행 추가 - 같은 원소 값 입력
df.loc[3] = 0
print(df)
"""
    수학  영어   음악   체육  국어
이름
서준  90  98   85  100  80
우현  80  89   95   90  80
인아  70  95  100   90  80
3    0   0    0    0   0
"""

#새로운 행 추가 - 여러 개의 원소 값 입력
df.loc[4] = ['동규', 90, 80, 70, 60]
print(df)
"""
    수학  영어   음악   체육  국어
이름
서준  90  98   85  100  80
우현  80  89   95   90  80
인아  70  95  100   90  80
3    0   0    0    0   0
4   동규  90   80   70  60
"""

#새로운 행 추가 - 기존 행 복사
df.loc['행5'] = df.loc[3]
print(df)
"""
    수학  영어   음악   체육  국어
이름
서준  90  98   85  100  80
우현  80  89   95   90  80
인아  70  95  100   90  80
3    0   0    0    0   0
4   동규  90   80   70  60
행5   0   0    0    0   0
"""

#기존 행 수정하기(modify element)
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
print("exam_data :: ", df)
print('=======================================')
print('\n')
"""
수학  영어   음악   체육
이름
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90
"""
df.iloc[0][3] = 33
print(df)
"""
    수학  영어   음악  체육
이름
서준  90  98   85  33
우현  80  89   95  90
인아  70  95  100  90
"""

df.loc['서준']['체육'] = 99
print(df)
"""
    수학  영어   음악  체육
이름
서준  90  98   85  99
우현  80  89   95  90
인아  70  95  100  90
"""

df.loc['서준', '체육'] = 90
print(df)
"""
    수학  영어   음악  체육
이름
서준  90  98   85  90
우현  80  89   95  90
인아  70  95  100  90
"""

df.loc['서준', ['음악', '체육']] = 50
print(df)
"""
    수학  영어   음악  체육
이름
서준  90  98   50  50
우현  80  89   95  90
인아  70  95  100  90
"""

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)
"""
    수학  영어   음악  체육
이름
서준  90  98  100  50
우현  80  89   95  90
인아  70  95  100  90
"""


#행, 열 위치 바꾸기
#형식 : DataFrame 객체.transpose() 또는 DataFrame 객체.T
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
df.set_index('이름', inplace=True)
print("exam_data :: ", df)
print('=======================================')
print('\n')
"""
    수학  영어   음악   체육
이름
서준  90  98   85  100
우현  80  89   95   90
인아  70  95  100   90
"""

#행, 열 위치 바꾸기
df = df.transpose() # transpose() : 행과 열을 바꾼다.
print(df)
"""
    이름   서준  우현   인아
수학   90  80   70
영어   98  89   95
음악   85  95  100
체육  100  90   90
"""


exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
ndf = df.set_index('이름') # inplace가 false이면 원본은 그대로 두고 새로운 객체를 반환한다.
print(ndf)

#index 초기화
ndf2 = ndf.reset_index()
print(ndf2)

# 덧셈, 뺄셈, 곱셈, 나눗셈 연산
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '국어':90, '영어':80})
print(student1)
print('\n')
print(student2)
print('\n')
addition = student1 + student2               #덧셈
subtraction = student1 - student2            #뺄셈
multiplication = student1 * student2         #곱셈
division = student1 / student2               #나눗셈
print(type(division))
result = pd.DataFrame([addition, subtraction, multiplication, division],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)