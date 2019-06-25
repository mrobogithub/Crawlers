import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import datetime
from time import sleep
import os
import sys
import selenium
from selenium import webdriver
import time
import matplotlib.pyplot as plt
%matplotlib inline
import matplotlib.font_manager as fm
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np
from PIL import Image


def ask_keyword():
    keyword = input('검색하고자 하는 키워드를 입력하세요 :      ') + '/'
    
    return keyword




keyword = ask_keyword()

#내가 보고자하는 인스타그램의 태그 검색 페이지
url =  'https://www.instagram.com/explore/tags/'
url  = url + keyword

#크롬을 쓰겠다. 
driver = webdriver.Chrome('./chromedriver')

#크롬에게 get -> 내가 원하는 검색어 포함 주소 입력
driver.get(url) 

#페이지 로딩 3초 대기
sleep(3)

#가장 첫 번째 게시물 클릭
driver.find_element_by_class_name('eLAPa').click() 
content_all = []

#원하는 횟수만큼 
count = 40
for i in range(count):
    print(i)
    clickmore_html = driver.page_source
    click_soup = BeautifulSoup(clickmore_html, 'lxml')
    try:
        contents = click_soup.find('div',{'class':'C4VMK'}).get_text()
#         imgurl = click_soup.find('div',{'class':'KL4Bh'}).find('img')['src']
        content_all.append(contents)
        driver.find_element_by_class_name('HBoOv').click() #HBoOv 태그는 next버튼을 의미하는거라서 이거 계속 50000번 클릭해서 데이터 모으기
    except:
        print('None contents here')
    sleep(0.4)
        
#읽은 파일들 텍스트파일에 저장
f = open(keyword[:-1] + '.txt','w') 
for i in content_all:
    f.write(i)
f.close()
