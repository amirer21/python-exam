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
# 3 데이터 표준화
import pandas as pd

## 3-1 단위 환산
df = pd.read_csv("./Data_full/auto-mpg.csv", header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.head(3))
print("\n")
print("=========================================")
'''
    mpg  cylinders  displacement horsepower  weight  acceleration  model year  origin                       name
0  18.0          8         307.0      130.0  3504.0          12.0          70       1  chevrolet chevelle malibu
1  15.0          8         350.0      165.0  3693.0          11.5          70       1          buick skylark 320
2  18.0          8         318.0      150.0  3436.0          11.0          70       1         plymouth satellite
'''

#mpg(mile per gallon)를 kpl(kilometer per liter)로 변환 (mpg_to_kpl = 0.425)
# 1 mile = 1.60934 km, 1 gallon = 3.78541 liter, 1mpg = 0.425 kpl
mpg_to_kpl = 1.60934 / 3.78541
df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head(3))
print("\n")
print("=========================================")
'''
    mpg  cylinders  displacement horsepower  weight  acceleration  model year  origin                       name       kpl
0  18.0          8         307.0      130.0  3504.0          12.0          70       1  chevrolet chevelle malibu  7.652571
1  15.0          8         350.0      165.0  3693.0          11.5          70       1          buick skylark 320  6.377143
2  18.0          8         318.0      150.0  3436.0          11.0          70       1         plymouth satellite  7.652571
'''
df['kpl'] = df['kpl'].round(2) #kpl 컬럼의 값을 소수점 아래 둘째 자리에서 반올림
print(df.head(3))
print("\n")
print("=========================================")
'''
    mpg  cylinders  displacement horsepower  weight  acceleration  model year  origin                       name   kpl
0  18.0          8         307.0      130.0  3504.0          12.0          70       1  chevrolet chevelle malibu  7.65
1  15.0          8         350.0      165.0  3693.0          11.5          70       1          buick skylark 320  6.38
2  18.0          8         318.0      150.0  3436.0          11.0          70       1         plymouth satellite  7.65
'''

#######################
# 03-2 자료형 변환
df = pd.read_csv("./Data_full/auto-mpg.csv", header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.head(3))
print("\n")
print("=========================================")

print(df.dtypes) #dtype: object
print("\n")

print(df['horsepower'].unique())
print("\n")
#? 물음표가 있는 값이 있다.
'''
['130.0' '165.0' '150.0' '140.0' '198.0' '220.0' '215.0' '225.0' '190.0'
 '170.0' '160.0' '95.00' '97.00' '85.00' '88.00' '46.00' '87.00' '90.00'
 '113.0' '200.0' '210.0' '193.0' '?' '100.0' '105.0' '175.0' '153.0'
 '180.0' '110.0' '72.00' '86.00' '70.00' '76.00' '65.00' '69.00' '60.00'
 '80.00' '54.00' '208.0' '155.0' '112.0' '92.00' '145.0' '137.0' '158.0'
 '167.0' '94.00' '107.0' '230.0' '49.00' '75.00' '91.00' '122.0' '67.00'
 '83.00' '78.00' '52.00' '61.00' '93.00' '148.0' '129.0' '96.00' '71.00'
 '98.00' '115.0' '53.00' '81.00' '79.00' '120.0' '152.0' '102.0' '108.0'
 '68.00' '58.00' '149.0' '89.00' '63.00' '48.00' '66.00' '139.0' '103.0'
 '125.0' '133.0' '138.0' '135.0' '142.0' '77.00' '62.00' '132.0' '84.00'
 '64.00' '74.00' '116.0' '82.00']
'''

#
import numpy as np

#replace(찾을값, 바꿀값) : 찾을값을 바꿀값으로 변경
df['horsepower'].replace('?', np.nan, inplace=True) #?을 np.nan으로 변경
#dropna() : 누락 데이터가 있는 행을 삭제
df.dropna(subset=['horsepower'], axis=0, inplace=True) #누락 데이터 행을 삭제
#astype() : 데이터의 자료형을 변환. object -> float
df['horsepower'] = df['horsepower'].astype('float') #문자열을 실수형으로 변환

print(df.dtypes)
print(df['horsepower'].dtypes) #dtype: float64
print("\n")
print(df['horsepower'].unique())
'''
[130. 165. 150. 140. 198. 220. 215. 225. 190. 170. 160.  95.  97.  85.
  88.  46.  87.  90. 113. 200. 210. 193. 100. 105. 175. 153. 180. 110.
  72.  86.  70.  76.  65.  69.  60.  80.  54. 208. 155. 112.  92. 145.
 137. 158. 167.  94. 107. 230.  49.  75.  91. 122.  67.  83.  78.  52.
  61.  93. 148. 129.  96.  71.  98. 115.  53.  81.  79. 120. 152. 102.
 108.  68.  58. 149.  89.  63.  48.  66. 139. 103. 125. 133. 138. 135.
 142.  77.  62. 132.  84.  64.  74. 116.  82.]
'''

#origin 문자열로 변환
print(df['origin'].unique())
'''
[1 3 2]
''' 

#replace()로 1은 USA, 2는 EU, 3은 JPN으로 변경
df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)
print(df['origin'].unique())
print(df['origin'].dtypes)
'''
['USA' 'JPN' 'EU']
object
'''

#origin 열의 자료형을 category로 변환
df['origin'] = df['origin'].astype('category') #문자열을 카테고리로 변환
print(df['origin'].dtypes)
'''
category
'''
print("\n")
print("=========================================")

#2.0.2
# pandas ver 2.x 이상 : 데이터프레임에 대한 통계 명령어 사용시 mean(numeric_only=True) 사용
print(pd.__version__) 

print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
'''
#무작위 데이터이므로 앞에 359, 186, 244 값은 다를 수 있음. index이다.
359    81
186    76
244    78
Name: model year, dtype: int64
187    76
130    74
69     72
Name: model year, dtype: category
Categories (13, int64): [70, 71, 72, 73, ..., 79, 80, 81, 82]
'''