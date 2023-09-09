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
# 4 데이터 범주화(카테고리) 처리

## 4.1 구간 분할
## 4.2 더미 변수


# 구간과 경계
# 구간 : 연속적인 데이터를 일정한 구간으로 나누는 것
# 경계 : 구간을 나누는 기준이 되는 값

import pandas as pd
import numpy as np


df = pd.read_csv("./Data_full/auto-mpg.csv", header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
                'acceleration','model year','origin','name']

df['horsepower'].replace('?', 'NaN', inplace=True) # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True) # 누락 데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float') # 문자열을 실수형으로 변환

df['horsepower'].fillna(0, inplace=True)
#df['horsepower'].replace('?', np.nan, inplace=True) #?을 np.nan으로 변경
count, bin_dividers = np.histogram(df['horsepower'], bins=3) #histogram 함수로 3개의 bin으로 나누는 경계값의 리스트 구하기. bins : 구간 개수
# 구간 경계값 리스트 출력
print(bin_dividers) 
#[ 0.  76.66666667  153.33333333  230.       ]
print("\n")
# 각 구간에 속하는 값의 개수 출력
print(count) 
#[109 247  42]
print("=========================================")


# 각각 구간의 이름을 지정
bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(x=df['horsepower'], # x : horsepower 열
                        bins=bin_dividers, # bins : 경계값 리스트
                        labels=bin_names, # labels : bin 이름
                        include_lowest=True) # include_lowest : 첫 경계값 포함
print(df[['horsepower', 'hp_bin']].head(15))
print("=========================================")
'''
    horsepower hp_bin
0        130.0   보통출력
1        165.0    고출력
2        150.0   보통출력
3        150.0   보통출력
4        140.0   보통출력
5        198.0    고출력
6        220.0    고출력
7        215.0    고출력
8        225.0    고출력
9        190.0    고출력
10       170.0    고출력
11       160.0    고출력
12       150.0   보통출력
13       225.0    고출력
14        95.0   보통출력
'''

## 04.2 더미 변수
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))
print("=========================================")
'''
      저출력   보통출력    고출력
0   False   True  False
1   False  False   True
2   False   True  False
3   False   True  False
4   False   True  False
5   False  False   True
6   False  False   True
7   False  False   True
8   False  False   True
9   False  False   True
10  False  False   True
11  False  False   True
12  False   True  False
13  False  False   True
14  False   True  False
'''

#sklearn : 머신러닝 패키지
#pip > pip install scikit-learn

from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder

label_encoder = preprocessing.LabelEncoder() # labelEncoder() : 레이블 인코더 생성
onehot_encoder = preprocessing.OneHotEncoder() # OneHotEncoder() : 원핫 인코더 생성

# labelEncoder로 문자열 범주를 숫자형 범주로 변환
onehot_encoder = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_encoder)
print(type(onehot_encoder))
print("=========================================")

# 2차원 행렬로 변환
onehot_encoder = onehot_encoder.reshape(len(onehot_encoder), 1)
print(onehot_encoder)
print(type(onehot_encoder)) 
print("=========================================")

#희소행렬로 변환
onehot_fitted = onehot_encoder.fit_transform(onehot_encoder)
print(onehot_fitted)
print(type(onehot_fitted))
print("=========================================")

mystr = 'Life is too short, you need python'
print(mystr[:4]) #--> Life
print(mystr[:5:2]) #--> Lf
print(mystr[::-1]) #--> nohtyp deen uoy ,trohs oot si efiL
print(mystr[-6:-1])#--> python