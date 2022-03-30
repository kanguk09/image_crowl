from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import urllib.request

## 다운로드 막아놔서 쓰는 코드
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

## 폴더 생성
def createFolder(directory):
  try:
    if not os.path.exists(directory):
      os.makedirs(directory)
  except OSError:
    print('Error:Creating directory.'+directory)


## 키워드 검색
keyword = input('키워드 작성: ')
foldername = './data/'+keyword+'_img_download'
createFolder(foldername)
chromedriver = 'C:/Users/kangu/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(1)



print(keyword,'검색')
driver.get('https://www.google.co.kr/imghp?hl=ko')

Keyword=driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
Keyword.send_keys(keyword)

driver.find_element_by_xpath('//*[@id="sbtc"]/button').click()

print(keyword+'스크롤중...........')
elem = driver.find_element_by_tag_name("body")
for i in range(60):
  elem.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.1)

try:
  driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[4]/div[2]/input').click()
  for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

except:
  pass

## 이미지 다운로드

links = []
images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
for image in images:
  if image.get_attribute('src')!=None:
    links.append(image.get_attribute('src'))
    
print(keyword+'찾은 이미지 개수:',len(links))
time.sleep(2)

filename = 0

def download_file(url):    
    urllib.request.urlretrieve(url, foldername+'/'+keyword+'_'+str(k+1)+'.jpg')  ## urlretrieve(url,경로/.형식)


for k,i in enumerate(links):
  url = i
  start = time.time()
  filename = keyword + '_'+str(k+1)+'.jpg'
  download_file(url)
  print(str(k+1)+'/'+str(len(links))+''+keyword+'  다운로드 중....')
print(keyword+'---다운로드 완료---')

driver.close()

