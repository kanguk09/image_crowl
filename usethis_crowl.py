import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

## 다운로드 막아놔서 쓰는 코드
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

search = "다먹고 남은 과자봉지"
foldername = './data/'+search+'_img_download'
driver = webdriver.Chrome('C:/Users/kangu/Downloads/chromedriver_win32/chromedriver.exe')

## 폴더 생성
def createFolder(directory):
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
  except OSError:
    print('Error:Creating directory.'+directory)
createFolder(foldername)


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
SAVE_FLAG = False
def timeout(limit_time): #timeout
    start = time.time()
    while True:
        if time.time() - start > limit_time or SAVE_FLAG:
            raise Exception('timeout. or image saved.')


# #키워드 검색
print(search,'검색')
driver.get('https://www.google.co.kr/imghp?hl=ko')

Keyword=driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
Keyword.send_keys(search)

driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()

## 페이지스크롤
print(search+'스크롤중...........')
elem = driver.find_element_by_tag_name("body")
for i in range(60):
  elem.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.1)

try:
  driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click() ##결과더보기 버튼 클릭
  for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

except:
  pass

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 0
for image in images:
    SAVE_FLAG = False
    timer = threading.Thread(target=timeout, args=(30,))
    try:
        image.click()
        #이미지의 XPath 를 붙여넣기 해준다. >> F12 를 눌러서 페이지 소스의 Element에서 찾아보면됨.
        imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        urllib.request.urlretrieve(imgUrl, foldername+'/'+ search + '_' +str(count) + ".jpg") #저장할 이미지의 경로 지정
        print('Save images : ', "images/"+ search + "_{0:04}".format(count) + ".jpg")
        SAVE_FLAG = True
        count += 1
        if timer.is_alive():
            timer.join()
    except Exception as e:
        if timer.is_alive():
            timer.join()
        pass
print('driver end. Total images : ', count)
driver.close()