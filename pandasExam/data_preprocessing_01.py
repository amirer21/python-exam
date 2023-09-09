#데이터 전처리란 데이터를 분석하기 좋은 형태로 만들어 주는 것을 말한다.
#영어로는 Data Preprocessing이라고 한다.

#데이터 전처리는 데이터 분석의 성능을 향상시키는데 중요한 역할을 한다.
#데이터 전처리를 하지 않으면 데이터 분석의 결과가 잘 나오지 않을 뿐만 아니라
#잘못된 결과를 도출할 수도 있다.

# 순서
# 누락 데이터 처리
# 중복 데이터 처리
# 데이터 표준화
# 데이터 범주화(카테고리) 처리
# 데이터 정규화
# 시계열 데이터 처리


###########
# 누락 데이터 처리

import seaborn as sns

df = sns.load_dataset('titanic')
#df.to_excel('titanic.xlsx', sheet_name='titanic', index=False)
print(df.head()) #head는 데이터의 처음 5개의 행을 출력한다.
"""
survived  pclass     sex   age  sibsp  parch     fare embarked  class    who  adult_male deck  embark_town alive  alone
0         0       3    male  22.0      1      0   7.2500        S  Third    man        True  NaN  Southampton    no  False
1         1       1  female  38.0      1      0  71.2833        C  First  woman       False    C    Cherbourg   yes  False
2         1       3  female  26.0      0      0   7.9250        S  Third  woman       False  NaN  Southampton   yes   True
3         1       1  female  35.0      1      0  53.1000        S  First  woman       False    C  Southampton   yes  False
4         0       3    male  35.0      0      0   8.0500        S  Third    man        True  NaN  Southampton    no   True
"""

#info()는 데이터의 간략한 정보를 출력한다.
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   survived     891 non-null    int64
 1   pclass       891 non-null    int64
 2   sex          891 non-null    object
 3   age          714 non-null    float64
 4   sibsp        891 non-null    int64
 5   parch        891 non-null    int64
 6   fare         891 non-null    float64
 7   embarked     889 non-null    object
 8   class        891 non-null    category
 9   who          891 non-null    object
 10  adult_male   891 non-null    bool
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object
 13  alive        891 non-null    object
 14  alone        891 non-null    bool
dtypes: bool(2), category(2), float64(2), int64(4), object(5)
memory usage: 80.7+ KB
None
"""

# 컬럼을 선택하고, 그 컬럼에 요소가 몇개씩 있는지 출력한다.
#df['deck'] 컬럼을 가져오고, value_counts()로 각각의 값이 몇개씩 있는지 출력
# dropna는 NaN값도 출력
nan_deck = df['deck'].value_counts(dropna=False) 
print("nan_deck :: ",nan_deck)
"""
deck
NaN    688
C       59
B       47
D       33
E       32
A       15
F       13
G        4
Name: count, dtype: int64
"""

#dropna는 NaN값을 제외하고 출력
nan_deck = df['deck'].value_counts(dropna=True) 
print("nan_deck True :: ",nan_deck)
"""
deck
C    59
B    47
D    33
E    32
A    15
F    13
G     4
"""


#head()는 데이터의 처음 5개의 행을 출력한다.
#isnull()은 NaN값이면 True, 아니면 False를 출력한다.
#sum()은 합계를 구한다. axis=0은 열을 기준으로 합계를 구한다.
print(df.head().isnull().sum(axis=0))
"""
survived       0
pclass         0
sex            0
age            0
sibsp          0
parch          0
fare           0
embarked       0
class          0
who            0
adult_male     0
deck           3
embark_town    0
alive          0
alone          0
dtype: int64
"""

## 누락 데이터 제거
### dropna()는 NaN 값이 있는 행을 편집한다.
### 기본 사용방법
#df.dropna(axis=0) : NaN값이 있는 행을 삭제한다.
#df.dropna(axis=1) : NaN값이 있는 열을 삭제한다.
#how : 'any'는 NaN값이 하나라도 있으면 삭제한다.
#how : 'all'은 모든 값이 NaN이면 삭제한다.
#thresh : NaN값이 thresh보다 작으면 삭제한다.
# subset : NaN값을 검사할 열의 이름을 리스트로 전달한다.
# inplace : True이면 df에 적용하고, False이면 df에 적용하지 않는다.
# 예 : df.dropna(subset=['age'], how='any', axis=0, inplace=True, thresh=500)


missing_df = df.isnull() #isnull()은 NaN값이면 True, 아니면 False를 출력한다.
"""
missing_df ::       survived  pclass    sex    age  sibsp  parch   fare  embarked  class    who  adult_male   deck  embark_town  alive  alone
0       False   False  False  False  False  False  False     False  False  False       False   True        False  False  False
1       False   False  False  False  False  False  False     False  False  False       False  False        False  False  False
2       False   False  False  False  False  False  False     False  False  False       False   True        False  False  False
3       False   False  False  False  False  False  False     False  False  False       False  False        False  False  False
4       False   False  False  False  False  False  False     False  False  False       False   True        False  False  False
..        ...     ...    ...    ...    ...    ...    ...       ...    ...    ...         ...    ...          ...    ...    ...
886     False   False  False  False  False  False  False     False  False  False       False   True        False  False  False
887     False   False  False  False  False  False  False     False  False  False       False  False        False  False  False
888     False   False  False   True  False  False  False     False  False  False       False   True        False  False  False
889     False   False  False  False  False  False  False     False  False  False       False  False        False  False  False
890     False   False  False  False  False  False  False     False  False  False       False   True        False  False  False
"""
    
print("missing_df :: ",missing_df)
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts() # Nan의 개수를 출력한다.
    try:
        print(col, " :: ", missing_count[True]) # Nan의 개수를 출력한다.
    except:
        print(col, " :: ", 0)
"""
survived  ::  0
pclass  ::  0
sex  ::  0
age  ::  177
sibsp  ::  0
parch  ::  0
fare  ::  0
embarked  ::  2
class  ::  0
who  ::  0
adult_male  ::  0
deck  ::  688
embark_town  ::  2
alive  ::  0
alone  ::  0
"""


## NaN 값이 500개 이상인 컬럼을 모두 삭제
df_thresh = df.dropna(axis=1, thresh=500) #NaN값이 500개 이상인 컬럼을 모두 삭제한다.
print(df_thresh.columns)
'''
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'embark_town', 'alive',
       'alone'],
      dtype='object')
'''

#subset : NaN값을 검사할 열의 이름을 리스트로 전달한다.
#how : 'any'는 NaN값이 하나라도 있으면 삭제한다.
df_age = df.dropna(subset=['age'], how='any', axis=0) #age 열에 나이 데이터가 없는 모든 행을 삭제한다.
print(len(df_age)) #714
print("=========================================")


######################

# 누락 데이터 치환 방법
print(df['age'].head(10)) #age 열의 첫 10개의 데이터를 출력한다.
print("\n")
print("=========================================")
#아래와 같이 Nan 값이 있는 행이 있다.
"""
0    22.0
1    38.0
2    26.0
3    35.0
4    35.0
5     NaN
6    54.0
7     2.0
8    27.0
9    14.0
Name: age, dtype: float64
"""

# fillna() : NaN값을 다른 값으로 변경한다.
## age 열의 NaN값을 다른 나이 데이터의 평균으로 변경한다.
mean_age = df['age'].mean(axis=0) # mean() : 평균을 구한다. axis=0은 열을 기준으로 평균을 구한다.
df['age'].fillna(mean_age, inplace=True) #age 열의 NaN값을 평균으로 변경한다.
print(df['age'].head(10)) #age 열의 첫 10개의 데이터를 출력한다.
print("\n")
print("=========================================")
'''
0    22.000000
1    38.000000
2    26.000000
3    35.000000
4    35.000000
5    29.699118
6    54.000000
7     2.000000
8    27.000000
9    14.000000
Name: age, dtype: float64
'''

print(df['embark_town'][825:830]) #embark_town 열의 825~830행의 데이터를 출력한다.
print("\n")
print("=========================================")

# embark_town 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환한다.
most_freq = df['embark_town'].value_counts(dropna=True).idxmax() #value_counts() : 각각의 값이 몇개씩 있는지 출력한다.
print(most_freq) #Southampton
print("\n")
print("=========================================")


df['embark_town'].fillna(most_freq, inplace=True) #embark_town 열의 NaN값을 most_freq로 변경한다.
print(df['embark_town'][825:830]) #embark_town 열의 825~830행의 데이터를 출력한다.
print("\n")
print("=========================================")
'''
825     Queenstown
826    Southampton
827      Cherbourg
828     Queenstown
829    Southampton
Name: embark_town, dtype: object
'''

#이웃하고 있는 값으로 바꾸기
df = sns.load_dataset('titanic')
print(df['embark_town'][825:830]) #embark_town 열의 825~830행의 데이터를 출력한다.
print("\n")
print("=========================================")
'''
825     Queenstown
826    Southampton
827      Cherbourg
828     Queenstown
829            NaN
Name: embark_town, dtype: object
'''

#inplace : True이면 df에 적용하고, False이면 df에 적용하지 않는다.
#inplace의 기능은 df = df.fillna(method='ffill')와 같다.
df['embark_town'].fillna(method='ffill', inplace=True) #embark_town 열의 NaN값을 바로 앞에 있는 값으로 변경한다.
print(df['embark_town'][825:830]) #embark_town 열의 825~830행의 데이터를 출력한다.
print("\n")
print("=========================================")
'''
825     Queenstown
826    Southampton
827      Cherbourg
828     Queenstown
829     Queenstown
Name: embark_town, dtype: object
'''