# 01.데이터 전처리
#### 01-1.서울시 스타벅스 매장 목록, 인구, 사업체 데이터에 시군구명, 시군구코드 추가

# 이 예제에서는 pandas의 merge() 함수를 사용하여 데이터를 병합한다.
# 수집한 2가지 데이터를 병합하여 분석에 사용할 데이터를 만든다.

# merge() 
# 두 개의 데이터프레임을 합쳐주는 함수이다. 두 데이터프레임에서 공통된 컬럼을 기준으로 병합한다.

# merge() 함수는 기본적으로 내부 조인(inner join)을 실행한다.
# 내부 조인은 두 데이터프레임에서 공통된 컬럼의 값이 일치하는 행만 병합하는 방식이다.

# merge() 함수의 how 옵션을 사용하면 조인 방식을 변경할 수 있다.
# how 옵션의 값으로 left, right, outer, inner를 사용할 수 있다.
# left : 왼쪽 데이터프레임을 기준으로 병합한다.
# right : 오른쪽 데이터프레임을 기준으로 병합한다.
# outer : 양쪽 데이터프레임에 모두 존재하는 데이터만 병합한다.
# inner : 한쪽 데이터프레임에만 존재하는 데이터는 병합하지 않는다.

# pivot_table() : 피벗 테이블 생성 함수
# 피벗 테이블을 생성하여, 데이터를 행과 열로 재구성한다.


import pandas as pd

seoul_starbucks = pd.read_excel('./data_output/seoul_starbucks.xlsx', header=0) #이 데이터는 앞에서 만든 데이터
seoul_starbucks.head()

# 스타벅스 주소 정보에서 시군구명 추출하고, '시군구명' 컬럼 추가
sgg_names = []
for address in seoul_starbucks['주소']:
    sgg = address.split()[1]
    sgg_names.append(sgg)
seoul_starbucks['시군구명'] = sgg_names
print("시군구 추가된 데이터 :: ", seoul_starbucks.head())
print("=============================================")
'''
시군구 추가된 데이터 ::      
          매장명       위도        경도       매장타입                          주소             전화번호 시군구명
0  역삼아레나빌딩  37.501087  127.043069  pin_general     서울특별시 강남구 언주로 425 (역삼동)  1522-3232  강남구
1   논현역사거리  37.510178  127.022223  pin_general    서울특별시 강남구 강남대로 538 (논현동)  1522-3232  강남구
2  신사역성일빌딩  37.513931  127.020606  pin_general    서울특별시 강남구 강남대로 584 (논현동)  1522-3232  강남구
3   국기원사거리  37.499517  127.031495  pin_general    서울특별시 강남구 테헤란로 125 (역삼동)  1522-3232  강남구
4  대치재경빌딩R  37.494668  127.062583  pin_reserve  서울특별시 강남구 남부순환로 2947 (대치동)  1522-3232  강남구
'''

# 엑셀 파일로 저장
seoul_starbucks.to_excel('./data_output/seoul_starbucks_list.xlsx', index=False)


###############################
# 스타벅스 분석 데이터 만들기
import pandas as pd

# 시군구 목록 데이터 불러오기
seoul_sgg = pd.read_excel('./api_files/seoul_sgg_list.xlsx', header=0)
print("시군구 데이터 :: ", seoul_sgg.head())  
print("=============================================")
'''
시군구 데이터 ::    
  시군구코드  시군구명         위도          경도
0  11320   도봉구  37.665861  127.031767
1  11380   은평구  37.617612  126.922700
2  11230  동대문구  37.583801  127.050700
3  11590   동작구  37.496504  126.944307
4  11545   금천구  37.460097  126.900155
'''

# 서울시 스타벅스 매장 목록 데이터 불러오기
seoul_starbucks = pd.read_excel('./data_output/seoul_starbucks_list.xlsx')
pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

print("스타벅스 데이터 :: ", seoul_starbucks.head())
print("=============================================")
'''
          매장명       위도        경도     매장타입                             주소        전화번호 시군구명 
0  역삼아레나빌딩  37.501087  127.043069  pin_general     서울특별시 강남구 언주로 42...    1522-3232   강남구
1    논현역사거리  37.510178  127.022223  pin_general     서울특별시 강남구 강남대로 5...   1522-3232   강남구
2  신사역성일빌딩  37.513931  127.020606  pin_general     서울특별시 강남구 강남대로 5...   1522-3232   강남구
3    국기원사거리  37.499517  127.031495  pin_general     서울특별시 강남구 테헤란로 1...   1522-3232   강남구
4   대치재경빌딩R  37.494668  127.062583  pin_reserve     서울특별시 강남구 남부순환로 ...  1522-3232   강남구
'''

#시군구별 스타벅스 매장 수 세기
#피벗 테이블로 시군구별 스타벅스 매장 수 세기
#pivot_table() : 피벗 테이블 생성 함수
#피벗 테이블은 데이터 열 중에서 두 개의 열을 각각 행 인덱스, 열 인덱스로 사용하여 데이터를 조회하여 펼쳐놓은 것
#데이터 중에서 자신이 원하는 데이터만을 가지고 원하는 행과 열에 데이터를 배치하여 새로운 보고서를 만드는 기능이다.
starbucks_sgg_count = seoul_starbucks.pivot_table(
                                                index='시군구명', #그룹화할 컬럼
                                                values='매장명', #결과에 포함할 컬럼
                                                aggfunc='count' #항목 수 세기
                                                ).rename(columns={'매장명':'스타벅스_매장수'}) #'매장명'을 '스타벅스_매장수'로 변경, rename(columns={'바꾸고 싶은 컬럼명':'바꿀 컬럼명'})

print("시군구별 스타벅스 매장 수 :: ", starbucks_sgg_count.head())
'''
시군구별 스타벅스 매장 수 ::        
        스타벅스_매장수
시군구명
강남구         88
강동구         17
강북구          6
강서구         25
관악구         12
'''

##  병합 : merge() 함수 사용
## 서울시 시군구 목록 데이터와 시군구별 스타벅스 매장 수 데이터 병합                                                
## merge(데이더프레임1, 데이터프레임2, how='left', on='기준컬럼명')
## how는 병합 방식을 지정한다.
## how : left, right, outer, inner
## left: 왼쪽 데이터프레임을 기준으로 병합
## right: 오른쪽 데이터프레임을 기준으로 병합
## outer : 양쪽 데이터프레임에 모두 존재하는 데이터만 병합
## inner : 한쪽 데이터프레임에만 존재하는 데이터는 병합하지 않음
## on : 기준이 되는 컬럼명
seoul_sgg = pd.merge(seoul_sgg, starbucks_sgg_count, how='left', on='시군구명')
print("seoul_sgg :: ", seoul_sgg.head())
'''
    시군구코드  시군구명         위도          경도  스타벅스_매장수
0   11320       도봉구      37.665861  127.031767         6
1   11380       은평구      37.617612  126.922700        13
2   11230       동대문구    37.583801  127.050700        10
3   11590       동작구      37.496504  126.944307        11
4   11545       금천구      37.460097  126.900155        12
'''


# 서울시 시군구별 인구 데이터 불러오기  
seoul_sgg_pop = pd.read_excel('./data_output/sgg_pop.xlsx')
print("seoul_sgg_pop :: ", seoul_sgg_pop.head())
'''
seoul_sgg_pop ::
  GIGAN SUM JACHIGU    SEDAE    GYE_1  NAMJA_1  YEOJA_1    GYE_2  NAMJA_2  YEOJA_2   GYE_3  NAMJA_3  YEOJA_3  SEDAEDANGINGU  N_65SEISANGGORYEONGJA
0  2023 1/4  합계      소계  4463385  9668008  4672170  4995838  9426404  4566299  4860105  241604   105871   135733           2.11                1690961
1  2023 1/4  합계     종로구    72679   152212    72819    79393   141060    68170    72890   11152     4649     6503           1.94                  28265
2  2023 1/4  합계      중구    63862   131390    63576    67814   120963    58699    62264   10427     4877     5550           1.89                  25353
3  2023 1/4  합계     용산구   109735   232482   112608   119874   217756   104640   113116   14726     7968     6758           1.98                  39478
4  2023 1/4  합계     성동구   133513   287240   139171   148069   280240   136233   144007    7000     2938     4062           2.10                  48238
'''


# 서울시 시군구별 인구 데이터와 시군구별 스타벅스 매장 수 데이터 병합
seoul_sgg = pd.merge(seoul_sgg, seoul_sgg_pop, how='left', on='시군구명')
print("seoul_sgg 111 :: ", seoul_sgg.head())
''''''

#서울시 시군구 목록 데이터에 서울시 시군구별 사업체 수 통계 데이터를 병합
seoul_sgg_biz = pd.read_excel('./data_output/sgg_biz.xlsx', header=0)
seoul_sgg = pd.merge(seoul_sgg, seoul_sgg_biz, how='left', on='시군구명')
print("seoul_sgg 222 :: ", seoul_sgg.head())
''''''

# 엑셀 파일로 저장
seoul_sgg.to_excel('./data_output/seoul_sgg_stat.xlsx', index=False)