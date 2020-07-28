from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import pandas as pd
from urllib.request import urlopen, Request

# selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("/Users/eum_dong/Downloads/chromedriver")

# "Instagram"에 접속한다
driver.get("https://www.instagram.com/")
driver.maximize_window()

time.sleep(3)

login_elem = driver.find_element_by_name("username")
login_elem.send_keys("eum1462@gmail.com", Keys.TAB, "eum6410!")
login_elem.submit()

time.sleep(5)


driver.get("https://www.instagram.com/explore/tags/음식물오염제거/")

time.sleep(5)

SCROLL_PAUSE_TIME = 1.0
reallink = []

while True:
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, 'lxml')

    for link1 in bsObj.find_all(name='div', attrs={"class":"Nnq7C weEfm"}):
        for i in range(3):
            title = link1.select('a')[i]
            real = title.attrs['href']
            reallink.append(real)
    last_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        else:
            last_height = new_height
            continue

num_of_data = len(reallink)

print('총 {0}개의 데이터를 수집합니다.'.format(num_of_data))
csvtext = []

for i in tqdm(range(num_of_data)):

    csvtext.append([])
    req = Request("https://www.instagram.com/p"+reallink[i], headers={'User-Agent': 'Mozila/5.0'})

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml', from_encoding='utf-8')
    soup1 = soup.find('meta', attrs={'property':"og:description"})

    reallink1 = soup1['content']
    reallink1 = reallink1[reallink1.find("@") + 1:reallink1.find(")")]
    reallink1 = reallink1[:20]

    if reallink1 == '':
        reallink1 = "Null"
    csvtext[i].append(reallink1)

    for reallink2 in soup.find_all('meta', attrs={'property':"instapp:hashtags"}):
        hashtags = reallink2['content'].rstrip(',')
        csvtext[i].append(hashtags)

    # csv로 저장

    data = pd.DataFrame(csvtext)
    data.to_csv('insta.txt', encoding='utf-8')

driver.close()

# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# notices = soup.select('div._7UhW9   xLCgt      MMzan  KV-D4          se6yk        hjZTB>span>div>a')
#
# for n in notices:
#     print(n.text())

# time.sleep(5)



# driver.quit()

# time.sleep(5)
# 페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
# assert "Google" in driver.title
# assert "Naver" in driver.title
# assert "Instagram" in driver.title

# driver.quit()
# 검색 입력 부분에 커서를 올리고
# 검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
# elem = driver.find_element_by_name("q")

# search_elem = driver.find_element_by_link_text("검색")
# search_elem.send_keys("음식")
# search_elem = driver.find_element_by_name("")
# 입력 부분에 default로 값이 있을 수 있어 비운다
# elem.clear()

# 검색어를 입력한다
# elem.send_keys("음식")

# 검색을 실행한다
# elem.submit()

# 검색이 제대로 됐는지 확인한다
# assert "No results found." not in driver.page_source

# 브라우저를 종료한다
# driver.close()
