from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
import datetime
import pandas as pd
from urllib.request import urlopen, Request

def insta_searching(word):
    url = 'https://www.instagram.com/explore/tags/' + word
    return url

def select_first(driver):
    first = driver.find_element_by_css_selector('div._9AhH0')
    first.click()
    time.sleep(3)

def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    try:
        content = soup.select('div.C4VMK > span')[0].text
    except:
        content = ''

    tags = re.findall(r'#[^\s#,\\]+', content)

    try:
        date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    except:
        date = ''

    data = [content, date, tags]
    return data

def move_next(driver):
    right = driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)

# selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("C:/chromedriver.exe")

word = 'love'
url = insta_searching(word)
driver.get(url)
time.sleep(5)

login_section = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button'
driver.find_element_by_xpath(login_section).click()
time.sleep(3)
elem_login = driver.find_element_by_name("username")
elem_login.clear()
elem_login.send_keys('eum1462@gmail.com')
elem_login = driver.find_element_by_name('password')
elem_login.clear()
elem_login.send_keys('eum6410!')
time.sleep(1)
xpath = '//*[@id="loginForm"]/div/div[3]/button/div'
driver.find_element_by_xpath(xpath).click()
time.sleep(4)

#3. 검색페이지 접속하기
driver.get(url)
time.sleep(4)
#4. 첫번째 게시글 열기
select_first(driver)
#5. 비어있는 변수(results) 만들기
results = []
#여러 게시물 크롤링하기
target = 9 #크롤링할 게시물 수
for i in range(target):
    data = get_content(driver) #게시물 정보 가져오기
    df = pd.DataFrame(data=data)
    df.to_csv('./out.csv',mode='a',header = True)
    move_next(driver)

driver.quit()