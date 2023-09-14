# selenium
# 동적 데이터 수집

## selenium 은 웹 브라우저를 제어하는 프레임워크
## 간단한 예제 코드를 통해 selenium으로 웹 브라우저의 태그를 찾고, 값을 가져오는 방법을 알아보자.

## send_keys() : 키보드 입력을 위한 메소드. 키보드를 입력하는 것처럼 웹 브라우저에 입력할 수 있다.
## find_element() : 하나의 요소를 찾음
## find_elements() : 여러개의 요소를 찾음

# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.naver.com/"

service = Service() # Selenium 4부터는 Service 객체를 생성해야 함  
#service의 구조는 selenium.webdriver.chrome.service.Service 클래스를 참고
# https://www.selenium.dev/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.service.html
# executable_path는 이 클래스의 생성자의 인자로 들어가는데, 이는 chromedriver의 경로를 의미함


options = webdriver.ChromeOptions() # ChromeOptions : 크롬 브라우저의 설정을 위한 객체
driver = webdriver.Chrome(service=service, options=options) # Chrome() : 크롬 브라우저를 실행하기 위한 객체
# serivce : 크롬 드라이버를 실행하기 위한 객체, options : 크롬 브라우저의 설정을 위한 객체

driver.get(url)

elem = driver.find_element(By.ID, "query")
elem.send_keys("파이썬")
elem.send_keys(Keys.ENTER)

############################################
## 태그 이름으로 찾기

driver.get(url)

# find_element : 하나의 요소를 찾음
# Tag name : 태그 이름으로 찾음
element = driver.find_element(By.TAG_NAME, "a")# a 태그를 찾음
elements = driver.find_elements(By.TAG_NAME, "a")

for idx, e in enumerate(elements):
    ele = e.get_attribute("href")# href 속성값을 가져옴
    print(idx, ele)
    
    time.sleep(1)
    
