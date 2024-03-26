"""
URL configuration for Investar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
