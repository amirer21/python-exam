# selenium
# 동적 데이터 수집

## pyperclip 설치
# pip install pyperclip

## pyperclip 사용법
# import pyperclip
## pyperclip을 사용하면 클립보드에 있는 문자열을 가져오거나 문자열을 클립보드에 복사할 수 있다.

# pyperclip.copy("복사할 문자열") : 문자열을 클립보드에 복사
# pyperclip.paste() : 클립보드에 있는 문자열을 가져옴

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

url = "http://naver.com"

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


try:
    #네이버 이동
    driver.get(url)
    # 로그인 버튼 클릭
    element = driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
    element.click()
    # id, pass 입력
    pyperclip.copy("아이디") # 클립보드에 복사
    driver.find_element(By.ID, "id").send_keys(Keys.CONTROL, 'v') # 복사한 내용을 붙여넣기 : ctrl + v
    pyperclip.copy("비밀번호") # 클립보드에 복사
    driver.find_element(By.ID, "pw").send_keys(Keys.CONTROL, 'v') # 복사한 내용을 붙여넣기 : ctrl + v
    driver.find_element(By.ID, "log.login").click()
    print(driver.page_source)
except Exception as e:
    print(e)

