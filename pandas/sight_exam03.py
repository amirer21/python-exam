import warnings
import pandas as pd
#MatPlotLib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import plotly.express as px

#경고 메시지 무시
warnings.simplefilter("ignore")

#외부에서 폰트를 불러오는 방법
fnot_path = "./font_data/malgun.ttf"
font_name = font_manager.FontProperties(fname=fnot_path).get_name()
rc('font', family=font_name)

# 이 실습 코드에서는 그래프에 여러 개의 선을 그리는 방법을 알아본다.

# 엑셀에서 데이터를 데이터프레임 변환
df = pd.read_excel('./Data_full/시도별_전출입_인구수.xlsx', engine= 'openpyxl', header=0)
df = df.fillna(method='ffill')
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1) #drop : 열 삭제
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True) #rename : 열 이름 바꾸기
df_seoul.set_index('전입지', inplace=True) #set_index : 행 인덱스 설정
sr_one = df_seoul.loc['경기도'] #loc : 행 인덱스를 기준으로 행 데이터 추출


###########################################################
#'충천남도', '경상북도', '강원도'
df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도']]
plt.style.use('ggplot') # 스타일 서식 지정. ggplot스타일 : 격자 무늬 스타일

fig = plt.figure(figsize=(20, 5))#그래프 크기 지정
ax1 = fig.add_subplot(1, 1, 1) #1행 3열의 1번째 그래프
ax1.plot(df_3.loc['충청남도',:], marker='o', markerfacecolor='green', markersize=10, color='olive', linewidth=2, label='서울 -> 충남')
ax1.plot(df_3.loc['경상북도',:], marker='o', markerfacecolor='blue', markersize=10, color='skyblue', linewidth=2, label='서울 -> 경북')
ax1.plot(df_3.loc['강원도',:], marker='o', markerfacecolor='red', markersize=10, color='magenta', linewidth=2, label='서울 -> 강원')

ax1.legend(loc='best') #범례 표시
ax1.set_title('서울 -> 충남, 경북, 강원 인구 이동', size=20) #제목 설정
ax1.set_xlabel('기간', size=12) #x축 이름 설정
ax1.set_ylabel('이동 인구수', size=12) #y축 이름 설정

plt.show() #그래프를 보여주는 것
