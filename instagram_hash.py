# import requests
# import bs4
#
# html = requests.get("https://www.instagram.com/explore/tags/%EC%9D%8C%EC%8B%9D/")
# bs_object = bs4.BeautifulSoup(html.text, "html.parser")
#
# insta_all_tag = bs_object.find("header", {"class": "id8oV  L3MTa"})
# for insta in insta_all_tag.findAll("div"):
#     print(insta.find("a", {"class": "LFGs8  xil3i"}))


# import time
# from selenium import webdriver
#
# # Optional argument, if not specified will search path.
# driver = webdriver.Chrome('/Users/eum_dong/Downloads/chromedriver')
# driver.get('http://www.google.com/xhtml');
# time.sleep(5)
#
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
#
# driver.quit()

from selenium import webdriver

path = "/Users/eum_dong/Downloads/chromedriver"  # ex. C:/downloads/chromedriver.exe

# 조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome(path)

#webdriver가 google 페이지에 접속하도록 명령
driver.get('https://www.google.com')

#webdriver를 종료하여 창이 사라진다
driver.close()



