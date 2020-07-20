from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# selenium의 webdriver로 크롬 브라우저를 실행한다
driver = webdriver.Chrome("/Users/eum_dong/Downloads/chromedriver")

# "Google"에 접속한다
driver.get("https://www.instagram.com/")

# 페이지의 제목을 체크하여 'Google'에 제대로 접속했는지 확인한다
# assert "Google" in driver.title
# assert "Naver" in driver.title

# 검색 입력 부분에 커서를 올리고
# 검색 입력 부분에 다양한 명령을 내리기 위해 elem 변수에 할당한다
# elem = driver.find_element_by_name("q")
elem = driver.find_element_by_name("username")
elem.send_keys("eum1462@gmail.com", Keys.TAB, "eum6410!")
elem.submit()
elem.
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
