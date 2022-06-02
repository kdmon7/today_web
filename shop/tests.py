from django.test import TestCase
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

# 다나와 사이트 검색

# 검색어 파이썬에서 입력 - 임시코드
searchKeyword = input("검색어 입력>>")
searchAddress = 'https://search.danawa.com/dsearch.php?query=' + searchKeyword

options = Options()
options.add_argument('headless');

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(5)

driver.get(searchAddress)

# bs4 초기화
soup = BeautifulSoup(driver.page_source, 'html.parser')

goods_list = soup.select('li.prod_item.prod_item_top5')

for v in goods_list:
    if v.find('div', class_='prod_main_info'):
        # 상품 모델명, 가격, 이미지
        name = v.select_one('p.prod_name > a').text.strip()
        # priceHolder = v.find("div",{"class":"top5_price"})
        price = v.select_one('div.top5_price > em ').text.strip()
        img_link = v.select_one('div.thumb_image > a > img').get('data-original')
        if img_link == None:
            img_link = v.select_one('div.thumb_image > a > img').get('src')
        print(name, " ||| ", price, "원 ||| ", img_link)
    print()

# 브라우저 종료
driver.close()

print(searchAddress)
