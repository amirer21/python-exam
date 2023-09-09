import pandas as pd
import lxml

#파일 읽어오기
#csv 파일 읽어오기
# 형식 : pd.read_csv('파일경로')
df = pd.read_csv("./Data_full/read_csv_sample.csv")
print(df)
print("\n")
"""
출력
   c0  c1  c2  c3
0   0   1   4   7
1   1   2   5   8
2   2   3   6   9
"""

#index_col : 특정 열을 행 인덱스로 지정
df2 = pd.read_csv("./Data_full/read_csv_sample.csv", index_col = None)
print(df2)
print("\n")

df3 = pd.read_csv("./Data_full/read_csv_sample.csv", index_col = 'c0')
print(df3)
print("\n")
"""c1  c2  c3
c0
0    1   4   7
1    2   5   8
2    3   6   9
"""


# excel 파일 읽어오기
# 형식 : pd.read_excel('파일경로')
#engine='openpyxl' : 엑셀을 읽어오기 위한 모듈 'openpyxl'을 지정. import openpyxl 와 같은 의미
# pip install openpyxl
df1 = pd.read_excel("./Data_full/남북한발전전력량.xlsx", engine='openpyxl') 
df2 = pd.read_excel("./Data_full/남북한발전전력량.xlsx", engine='openpyxl', header=None)
print(df1)
print("\n")
print(df2)

#json 파일 읽어오기
# 형식 : pd.read_json('파일경로')
df = pd.read_json("./Data_full/read_json_sample.json")
print(df)
print("\n")

#html 파일 읽어오기
# 형식 : pd.read_html('파일경로')
#pip install lxml
df1 = pd.read_html("./Data_full/sample.html")
print(df1)
print("\n")

print(len(df1)) #<table>태그의 갯수가 몇개인지 확인
print("\n")

for i in range(len(df1)):
    print("df1[%d]" % i)
    print(df1[i])
    print("\n")
    
df1 = df1[1]
#set_index : 특정 열을 행 인덱스로 지정, name열을 행 인덱스로 지정
df1.set_index(['name'], inplace=True)
print(df1)
print("\n")


#to csv and excel
data = {'name' : ['Jerry', 'Riah', 'Paul'], 'algol' : ["A", "A+", "B"], 'basic' : ["C", "B", "B+"], 'c++' : ["B+", "C", "C+"],}
df = pd.DataFrame(data)
#set_index : 특정 열을 행 인덱스로 지정
df.set_index('name', inplace=True)
print(df)

df.to_csv("./Data_full/df_sample22.csv")
df.to_excel("./Data_full/df_sample22.xlsx")


df = pd.read_csv("./Data_full/auto-mpg.csv", header=None)
# 열 이름 지정 .columns = [열1, 열2, 열3, ...]
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']
print(df.head())
"""
     mpg  cylinders  displacement horsepower  weight  acceleration  model year  origin                       name
0  18.0          8         307.0      130.0  3504.0          12.0          70       1  chevrolet chevelle malibu
1  15.0          8         350.0      165.0  3693.0          11.5          70       1          buick skylark 320
2  18.0          8         318.0      150.0  3436.0          11.0          70       1         plymouth satellite
3  16.0          8         304.0      150.0  3433.0          12.0          70       1              amc rebel sst
4  17.0          8         302.0      140.0  3449.0          10.5          70       1                ford torino
    
"""
print("\n")
print(df.tail())
"""
          mpg  cylinders  displacement horsepower  weight  acceleration  model year  origin             name
393  27.0          4         140.0      86.00  2790.0          15.6          82       1  ford mustang gl
394  44.0          4          97.0      52.00  2130.0          24.6          82       2        vw pickup
395  32.0          4         135.0      84.00  2295.0          11.6          82       1    dodge rampage
396  28.0          4         120.0      79.00  2625.0          18.6          82       1      ford ranger
397  31.0          4         119.0      82.00  2720.0          19.4          82       1       chevy s-10
"""

print(df.dtypes) #dtypes : 데이터프레임의 데이터 타입을 확인
print("\n")

"""
mpg             float64
cylinders         int64
displacement    float64
horsepower       object
weight          float64
acceleration    float64
model year        int64
origin            int64
name             object
dtype: object
"""

print(df.mpg.dtypes) #"mpg"라는 열의 데이터 타입 출력
print("\n")
"""
float64
"""

print(df.describe(include='all')) #describe() : 데이터프레임의 기초 통계량 출력, include='all' : 모든 열에 대한 기초 통계량 출력. 기초 통계량이란 평균, 표준편차, 최소값, 최대값, 중간값 등을 의미
#include의 속성. unique : 열에 대한 고유값 개수, top : 가장 많이 나온 고유값, freq : 가장 많이 나온 고유값의 빈도수
print(df.count())
print('\n')
print(type(df.count()))
print('\n')

unique_values = df['origin'].value_counts() # value_counts() : 고유값 빈도수
print(unique_values)
print('\n')

# 평균값
'''
print(df.mean())
print('\n')


print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())'''