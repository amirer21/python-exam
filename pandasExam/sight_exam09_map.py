import pandas as pd
import folium
import json

## 경기도 인구변화 데이터
file_path = './Data_full/경기도인구데이터.xlsx'
df = pd.read_excel(file_path, index_col='구분', engine='openpyxl') #index_col : 특정 열을 행 인덱스로 지정
df.columns = df.columns.map(str) #열 이름의 자료형을 문자열로 변경

## 경기도 시군구 경계 정보
geo_path = './Data_full/경기도행정구역경계.json'
try:
    geo_data = json.load(open(geo_path, encoding='utf-8')) 
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig')) 
    
## 경기도 지도 만들기 - 2007
g_map = folium.Map(location=[37.5502, 126.982], tiles='Stamen Terrain', zoom_start=9) #tiles는 지도 스타일, zoom_start는 확대 정도
year = '2007' # 엑셀에서 2007년 데이터만 추출

## Choropleth 클래스로 단계구분도 표시하기
folium.Choropleth(geo_data=geo_data, # geo_data : json 파일 경로
                    data = df[year], # data : 표시하려는 데이터
                    columns = [df.index, df[year]], #열 지정
                    fill_color = 'YlOrRd', #PuRd, YlGnBu
                    fill_opacity = 0.7, #투명도
                    line_opacity = 0.3, #경계 선 투명도
                    threshold_scale=[10000, 100000, 300000, 500000, 700000], #범례 스케일
                    key_on='feature.properties.name', #json 파일 내부의 정보 중에서, 지도를 표시하기 위한 지역 이름의 정보
                    ).add_to(g_map)

    
g_map.save('./output_file/gyonggi_population_'+ year + '.html') #지도 객체를 html 파일로 저장
print("g_map :: ", g_map)


## 경기도 지도 만들기 - 2017
g_map = folium.Map(location=[37.5502, 126.982], tiles='Stamen Terrain', zoom_start=9) #tiles는 지도 스타일, zoom_start는 확대 정도
year = '2017' # 엑셀에서 2017년 데이터만 추출

## Choropleth 클래스로 단계구분도 표시하기
folium.Choropleth(geo_data=geo_data, # geo_data : json 파일 경로
                    data = df[year], # data : 표시하려는 데이터
                    columns = [df.index, df[year]], #열 지정
                    fill_color = 'YlOrRd', #PuRd, YlGnBu
                    fill_opacity = 0.7, #투명도
                    line_opacity = 0.3, #경계 선 투명도
                    threshold_scale=[10000, 100000, 300000, 500000, 700000], #범례 스케일
                    key_on='feature.properties.name', #json 파일 내부의 정보 중에서, 지도를 표시하기 위한 지역 이름의 정보
                    ).add_to(g_map)
    
g_map.save('./output_file/gyonggi_population_'+ year + '.html') #지도 객체를 html 파일로 저장
print("g_map :: ", g_map)