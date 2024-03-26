#파이썬 Django 웹 프로그래밍 (1) : 장고 웹 프로젝트 시작하기

# 1. 장고 설치
# 설치 : pip install django
# 경로 : DjangoExam/mySite

# django-admin : 장고 프로젝트를 생성하거나 관리하는 커맨드라인 도구
#django-admin startproject Investar

# 2. 장고 프로젝트 생성
#python manage.py migrate : 데이터베이스 초기화

#  : 서버 실행
#python manage.py runserver 0.0.0.0:8000


# 프로젝트 생성
# django-admin startproject mySite

# 프로젝트 기본구조
# mySite
#     ㄴ mySite
#         ㄴ __init__.py : 해당 디렉터리가 패키지의 일부임을 알려주는 역할
#         ㄴ settings.py : 웹사이트 설정
#         ㄴ urls.py : 웹사이트의 URL과 뷰를 연결하는 URLconf 
#         ㄴ wsgi.py : WSGI 호환 웹 서버의 진입점을 작성하는 파일
#     ㄴ manage.py : 장고 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인의 유틸리티
# 여기에서 mySite가 프로젝트의 전반적인 설정을 담당하는 디렉터리이고 manage.py는 프로젝트 관리를 위한 커맨드라인 유틸리티이다.


# 서버 실행
# python manage.py runserver 0.0.0.0:8000
# 또는
# python manage.py startapp hello

# 프로젝트 환경 설정

## Host IP 설정
## 파일 : settings.py
'''
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
'''



## 장고 어플리케이션 생성
### python manage.py startapp hello
### hello 라는 이름의 앱 생성
### python manage.py migrate : 데이터베이스 초기화


### 어플리케이션 등록
### 파일 : settings.py
### INSTALLED_APPS = [...,'hello']

### URLconf 설정
### 파일 : urls.py
## import : hello/views.py를 import
### views.py에 있는 sayHello 함수를 사용하기 위해 hello/views.py를 import
### from hello import views
## urlpatterns = [..., path('hello/', views.sayHello)]
## /hello 로 요청이 들어오면 views.sayHello 함수를 호출한다.views.py에 있는 sayHello 함수를 호출한다.

#변경 전
'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
'''

#변경 후 
#hello 앱의 views.py에 있는 sayHello 함수를 호출한다.
# url로 접근할때, re_path를 사용하면 정규표현식을 사용할 수 있다.
# ^(?P<name>[A-Z][a-z]*)/$ (정규표현식) : 대문자로 시작하고 소문자로 끝나는 문자열
# 예: http://127.0.0.1:8000/Hello/
# URL Path에 대문자로 시작하고 소문자로 끝나는 문자열을 입력하면 views.py에 있는 sayHello 함수를 호출한다.
'''
from django.contrib import admin
from django.urls import path, re_path #re_path : 경로에 정규표현식을 사용하기 위해 추가
from hello import views #hello 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<name>[A-Z][a-z]*)/$', views.sayHello), #규칙 : 대문자로 시작하고 소문자로 끝나는 문자열. # P: parameter <name>: name이라는 이름으로 파라미터를 받겠다.
]
'''


#잠깐!
## 정규표현식
# ^ : 문자열의 시작
# $ : 문자열의 끝
# . : 임의의 문자 1개
# * : 앞 문자가 0개 이상
# + : 앞 문자가 1개 이상
# ? : 앞 문자가 없거나 1개
# [] : 문자의 집합이나 범위([a-z]: a부터 z까지, [^0-9]: 숫자가 아닌 문자)
# {} : 앞 문자의 개수({2}: 2개, {2,4}: 2개 이상 4개 이하)
# () : 그룹화(1개의 문자처럼 인식)
# | : or 연산
# \d : 숫자([0-9]와 동일). d는 digit의 약자
# \D : 숫자가 아닌 것([0-9]를 제외한 문자)
# \s : 공백 문자(띄어쓰기, 탭, 엔터 등). s는 space의 약자
# \S : 공백 문자가 아닌 것
# \w : 알파벳 대소문자, 숫자([a-zA-Z0-9]와 동일). w는 word의 약자
# \W : non alpha-numeric 문자([a-zA-Z0-9]를 제외한 문자)
# (?P<이름>...) : 그룹에 이름을 지정
# (?P=이름) : 지정한 그룹 참조


## view.py 수정 하기

### 생성된 앱의 기본 코드는 다음과 같다.
# render : 템플릿을 로딩할 때 사용하는 함수
# 파일은 빈 파일이다. 이제 추가해보자.
#수정 전
'''
from django.shortcuts import render

# Create your views here.
'''

#수정 후
'''
from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request, name):
    html = '<h1>Hello, {}!</h1>'.format(name)
    return HttpResponse(html)
'''

## 접속해보자.


#####################
## 관리자 페이지
# http://localhost:8000/admin

# 관리자 계정 생성
#python manage.py createsuperuser
#ID : admin
#PW : 1111
# http://127.0.0.1:8000/admin/ 접속


#####################
#파이썬 Django 웹 프로그래밍 (2) : 장고 템플릿 시스템 index.html

# index 앱 기본구조
# index
#     ㄴ migrations : 데이터베이스 마이그레이션 파일이 저장되는 디렉터리
#         ㄴ __init__.py
#     ㄴ static : 정적 파일이 저장되는 디렉터리
#         ㄴ index
#             ㄴ style.css
#     ㄴ templates : html 템플릿 파일이 저장되는 디렉터리
#         ㄴ index
#             ㄴ index.html
#     ㄴ __init__.py
#     ㄴ admin.py   : 관리자 페이지에서 index 앱을 관리하기 위한 설정 파일
#     ㄴ apps.py    : index 앱의 정보를 저장하는 설정 파일
#     ㄴ models.py  : index 앱에서 사용하는 모델을 정의하는 파일
#     ㄴ tests.py   : index 앱의 테스트를 작성하는 파일
#     ㄴ views.py   : index 앱의 뷰를 정의하는 파일


#(1) index app 생성
#cd \mySite\Investar
#python manage.py startapp index

#(2) settings.py에 앱 등록
# 경로 : DjangoExam/mySite/Investar/Investar/settings.py
# INSTALLED_APPS = [...,'index']

'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello', #hello 추가
    'index', #index 추가
]
'''
#(3) urls.py에 index app의 url 추가
# 경로 : DjangoExam/mySite/Investar/Investar/urls.py
# from index import views as index_views #index 추가
# urlpatterns = [..., path('index/', index_views.main_view)]


'''
from django.contrib import admin
from django.urls import path, re_path #re_path : 경로에 정규표현식을 사용하기 위해 추가
from hello import views #hello 추가
from index import views as index_views #index 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<name>[A-Z][a-z]*)/$', views.sayHello), #규칙 : 대문자로 시작하고 소문자로 끝나는 문자열. # P: parameter <name>: name이라는 이름으로 파라미터를 받겠다.
    path('index/', index_views.main_view), #index 추가
]

'''

#(4) index/views.py에 main_view 함수 추가
# 경로 : DjangoExam/mySite/index/views.py
#def main_view(request):
#   return render(request, 'index.html')

'''
from django.shortcuts import render

def main_view(request):
    return render(request, 'index.html')

'''

#(5) index/templates/index.html 생성
### index 앱의 templates 디렉터리를 생성하고 index.html 파일을 생성한다.
#경로 : \mySite\Investar\index\templates\index.html
'''

{% load static %} 
<html>
    <head>
        <title>This is title.</title> 
		<link rel="stylesheet" href={% static "index/style.css" %} />
    </head>
    <body>
        <h1>This is heading1 text.</h1>
        <h2>This is heading2 text.</h2>
        <h3>This is heading3 text.</h3>
        <p>This is a paragraph.</p>
        This is plain text.<br /> 
        <b>This is bold text.</b><br />
        <i>This is Italic text.</i><br />
        <s>This is strike text.</s><br />
        <ol>
            <li>the first orderd list</li>
            <li>the second orderd list</li>
            <li>the third orderd list</li>
        </ol>
        <ul>
            <li>unorderd list</li>
            <li>unorderd list</li>
            <li>unorderd list</li>
        </ul>
        <table border=1>
            <tr>
                <th>table header 1</th>
                <th>table header 2</th>
                <th>table header 3</th>
            </tr>
            <tr>
                <td>table data 4</td>
                <td>table data 5</td>
                <td>table data 6</td>
            </tr>
            <tr>
                <td>table data 7</td>
                <td>table data 8</td>
                <td>table data 9</td>
            </tr>
        </table><br />
        <a href="https://www.djangoproject.com">Visit Django homepage!<br />
        <img src={% static "index/Django_Logo.jpg" %} /></a>
    </body>
</html>

'''

## 접속해보기
### http://127.0.0.1:8000/index/
#####################

#파이썬 Django 웹 프로그래밍 (2) : 계좌 잔고 확인 페이지

#기본적인 순서는 다음과 같다.
# 1. balance 어플리케이션 생성
# 2. settings.py에 앱 등록
# 3. URLconf 설정
# 4. views.py에 get_data, main_view 함수(잔고 확인 페이지에서 주식 정보를 조회하는 함수) 추가
# 5. html : templates/balance.html 생성
# 6. css : static/b_style.css 생성
# 7. 접속해보기 : http://127.0.0.1:8000/balance/?035420=20&005930=100 (/balance/?주식 코드=주식 수량&주식 코드=주식 수량)

# balance 앱 기본구조
# balance
#     ㄴ migrations : 데이터베이스 마이그레이션 파일이 저장되는 디렉터리
#         ㄴ __init__.py
#     ㄴ static : 정적 파일이 저장되는 디렉터리
#         ㄴ balance
#             ㄴ b_style.css
#     ㄴ templates : html 템플릿 파일이 저장되는 디렉터리
#         ㄴ balance
#             ㄴ balance.html
#     ㄴ __init__.py
#     ㄴ admin.py   : 관리자 페이지에서 balance 앱을 관리하기 위한 설정 파일
#     ㄴ apps.py    : balance 앱의 정보를 저장하는 설정 파일
#     ㄴ models.py  : balance 앱에서 사용하는 모델을 정의하는 파일
#     ㄴ tests.py   : balance 앱의 테스트를 작성하는 파일
#     ㄴ views.py   : balance 앱의 뷰를 정의하는 파일


#1. balance 어플리케이션 생성

# cd \mySite\Investar
# python manage.py startapp balance

#2. settings.py에 앱 등록
# INSTALLED_APPS = [...,'balance']

#3. URLconf 설정
# 파일 : urls.py
## import : balance/views.py를 import
## urlpatterns = [..., path('balance/', views.main_view)]

'''
from django.contrib import admin
from hello import views #hello 추가
from django.urls import path, re_path #re_path 추가
from index import views as index_views #index 추가
from balance import views as balance_views #balance 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<name>[A-Z][a-z]*)/$', views.sayHello), #규칙 : 대문자로 시작하고 소문자로 끝나는 문자열. # P: parameter <name>: name이라는 이름으로 파라미터를 받겠다.    
    path('index/', index_views.main_view), #index 추가
    path('balance/', balance_views.main_view), #balance 추가
]

'''


#views.py 추가
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from django.shortcuts import render


def get_data(symbol):
    """
        symbol에 해당하는 주식에 대한 현재 가격, 등락률을 반환한다.
        
        Args:
            symbol(str): 주식의 심볼
        Returns:
            cur_price(str): 주식의 현재가
            cur_rate(str): 주식의 등락률
            stock_name(str): 주식의 이름    
    """
    url = 'http://finance.naver.com/item/sise.nhn?code={}'.format(symbol)
    with urlopen(url) as doc:
        soup = BeautifulSoup(doc, "lxml", from_encoding="euc-kr")#BeautifulSoup : html을 파싱하는 라이브러리
        cur_price = soup.find('strong', id='_nowVal') #_nowVal : 현재가
        cur_rate = soup.find('strong', id='_rate') #_rate : 등락률
        stock = soup.find('title') #title : 주식 이름
        print(stock)
        stock_name = stock.text.split(':')[0].strip()
        print(stock_name)
        return cur_price.text, cur_rate.text.strip(), stock_name
    
def main_view(request):
    """
        사용자가 입력한 주식의 심볼과 수량에 대한 정보를 가져와서
        현재가, 등락률, 주식 이름을 조회한 후 이를 템플릿에 전달한다.
        Args:
            request(HttpRequest): HttpRequest 객체
        Returns:
            render : 템플릿(html : balance.html)에 조회한 주식 정보를 전달한다.            
    """
    #mylist = [['035420', '20'], ['005930','100']]
    querydict = request.GET.copy()
    mylist = querydict.lists()
    rows = []
    total = 0
    for x in mylist:
        cur_price, cur_rate, stock_name = get_data(x[0]) #get_data : 주식의 현재가, 등락률, 주식 이름을 조회
        price = cur_price.replace(',', '')
        stock_count = format(int(x[1][0]), ',')
        sum = int(price) * int(x[1][0])
        stock_sum = format(sum, ',')
        rows.append([stock_name, x[0], cur_price, stock_count, cur_rate, stock_sum])
        total = total + int(price) * int(x[1][0])
    total_amount = format(total, ',')
    values = {'rows' : rows, 'total' : total_amount}
    print(values)
    return render(request, 'balance.html', values)
'''






#html 
#css static 파일을 사용하기 위해 {% static 'xxx.css%}를 추가한다.
#<link rel="stylesheet" href={% static "balance/style.css" %} />
#static : static 파일을 찾는 경로를 지정하는 템플릿 태그
#static 키워드는 settings.py에 설정된 STATICFILES_DIRS에 지정된 경로에서 static 파일을 찾는다.

#balance.html
'''
{% load static %}
<html>
    <head>
        <title>Balance: {{ total }}</title>  <!-- ① --> 
        <link rel="stylesheet" href="{% static 'b_style.css' %}"/>
    </head>
    <body>
         <table>
            <tr>
                <th>종목명</th>
                <th>종목코드</th>
                <th>현재가</th>
                <th>주식수</th>
                <th>등락률</th>
                <th>평가금액</th>
            </tr>
            {% for row in rows %}
            <tr>
                {% for x in row %}
                <td>{{ x }}</td>  <!-- ② -->
                {% endfor %}
            </tr>
            {% endfor %}
            <tr>
                <th colspan=3>계좌 잔고</th>
                <th colspan=3>{{ total }}</th>  <!-- ③ -->
            </tr>
        </table>
    </body>
</html>
'''


#####################
#2023.10.23 추가
# balance 추가
#python manage.py startapp balance


#conda 가상환경 목록보기
#conda env list

#가상환경 생성하기
#conda create -n 가상환경이름 python=버전
#conda create --name myenv python=3.7

#가상환경 활성화하기
#conda activate 가상환경이름
#conda activate myenv

#필요한 패키지 설치하기
#conda install 패키지이름
#conda install pandas
#conda install tensorflow
#conda install jupyter notebook

#가상환경 지우기
#conda env remove -n 가상환경이름