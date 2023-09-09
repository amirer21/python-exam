#import warnings
#import matplotlib.pyplot as plt
#from matplotlib import font_manager, rc
#import plotly.express as px
#import seaborn as sns
from folium.map import Popup
import pandas as pd
import folium

#2023.09.08
"""
#지도 시각화

#folium은 지도를 그리는 패키지
#python pip
#pip install folium
#ananconda prompt에서 설치하려면 아래 명령어를 입력
#conda install -c conda-forge folium
엑셀 파일에서 위도, 경도 데이터를 읽어서 지도에 마커를 표시한다.
불러온 엑셀 파일의 첫번째 열은 대학교 이름, 두번째 열은 위도, 세번째 열은 경도 데이터이다.
html 파일로 저장하여 웹 브라우저에서 지도를 확인한다.
"""

# 지도에 마커 표시하고, 이름을 팝업으로 표시하기(팝업설정)
pf =pd.read_excel('./Data_full/서울지역_대학교_위치.xlsx') #위도와 경도 데이터를 가진 엑셀 파일
seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12) #지도 객체 생성

for name, lat, lng in zip(pf['이름'], pf['위도'], pf['경도']): #name: 대학교 이름, lat: 위도, lng: 경도, zip: 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환
    iframe = folium.IFrame(name, width=200, height=50) #IFrame : html 태그를 지원하는 함수, width, height : 크기
    popup = folium.Popup(iframe, max_width=600) #Popup : 마커를 클릭했을 때 나오는 팝업창
    folium.Marker([lat, lng], popup=popup).add_to(seoul_map)   #Marker : 지도에 마커를 표시하는 함수, add_to(지도객체) : 지도에 마커를 추가하는 함수
    
seoul_map.save('./output_file/seoul_colleges1.html') #지도 객체를 html 파일로 저장

#############################
#CircleMarker로 표시하기
pf =pd.read_excel('./Data_full/서울지역_대학교_위치.xlsx') #위도와 경도 데이터를 가진 엑셀 파일
seoul_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12) #지도 객체 생성

for name, lat, lng in zip(pf['이름'], pf['위도'], pf['경도']): #name: 대학교 이름, lat: 위도, lng: 경도, zip: 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환
    folium.CircleMarker([lat, lng], #CircleMarker : 원형 마커를 표시하는 함수
                        radius=10, #radius : 원의 반지름
                        color='brown', #color : 원의 색상
                        fill=True, #fill : 원을 채우는지 여부
                        fill_color='coral', #fill_color : 원을 채우는 색상
                        fill_opacity=0.7, #fill_opacity : 투명도
                        popup=name#popup : 팝업창에 표시할 내용
                        ).add_to(seoul_map)   #add_to(지도객체) : 지도에 마커를 추가하는 함수
    
seoul_map.save('./output_file/seoul_colleges2.html') #지도 객체를 html 파일로 저장
print("seoul_map :: ", seoul_map)
