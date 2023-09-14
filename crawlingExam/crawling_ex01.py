# Request
# Urllib
# BeautifulSoup
# selenium


## requests 는 URL에 접속하고, 상태코드를 확인하고, HTML을 가져오는 역할을 한다.

# Request

import requests

# 정상적인 경우
res = requests.get("http://naver.com")
print("응답코드 :", res.status_code) # 200이면 정상

# 정상적이지 않은 경우
res = requests.get("http://yyy.tistory.com")
if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드", res.status_code, "]")
    
res = requests.get("http://naver.com")
res.raise_for_status() # 문제가 생기면 바로 프로그램 종료
print("정상 입니다.")
print(len(res.text))
#print(res.text)


## Urllib은 URL에 접속하고, HTML을 가져오는 역할을 한다.
## requests와 비슷한 역할을 한다.
#Urllib
from urllib.request import urlopen

url = "http://naver.com"
html = urlopen(url)
#print(html.read())

from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

try:
    #html = urlopen("http://www.google.com/kim.html") #HTTPError
    html = urlopen("http://www.google.com/test22.html") #URLError
except HTTPError as e:
    print(e)
except URLError as e:
    print("서버를 찾을 수 없습니다.")
else:
    print("성공")
    
    
#############################################

## BeautifulSoup는 가져온 HTML을 파싱하는 역할을 한다.
## 파싱이란 HTML을 분석해서 필요한 데이터만 추출하는 것을 말한다.
## 기본 사용법은 다음과 같다.
## BeautifulSoup(HTML데이터, 파싱방법)
## 파싱방법은 html.parser, lxml 등이 있다.

## BeautifulSoup은 find와 findAll을 제공한다.
## find : 하나만 찾는다.
## findAll : 여러개 찾는다. 

## BeautifulSoup - find & findAll
import bs4

html_str = "<html><div>hello</div></html>"
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))

##
import bs4
html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")
print(ul)

# find <li> tag, get text
li = ul.find("li")
print(li)
print(li.text)

# find all <li> tag, get text
lis = ul.findAll("li")
print(lis)
print(lis[1])
print(lis[1].text)

#############################################

## BeautifulSoup - find (태그, 클래스로 찾기)
import bs4

html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>   
        </ul>
    </body>
</html>
"""

## 태그로 찾기
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")   
print(ul)
print("=====================================")

## 클래스로 찾기
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul", {"class":"reply"})
print(ul)
print("=====================================")