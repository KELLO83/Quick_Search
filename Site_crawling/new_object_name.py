from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from bs4 import BeautifulSoup

from nltk.tokenize import word_tokenize # 자연어 처리 NLP
from collections import Counter
import nltk
import re  # 정규표현식 필터링

def upload_image_and_extract_keyword(image_path) -> str:
    """ IMAGE_PATH : 이미지 경로를 입력받습니다 안전하게 절대경로로 입력받는것을 권장합니다"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")

    lens_icon = driver.find_element(By.CSS_SELECTOR, "svg.Gdd5U")
    lens_icon.click()
    time.sleep(1)

    # 파일 입력 요소 선택
    file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
    # WebDriverWait를 사용하여 특정 요소가 로드될 때까지 대기
    time.sleep(1)


    # 이미지 파일의 로컬 경로 지정
    file_input.send_keys(image_path)
    time.sleep(2)
    try:
        button_is_existed = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/a')
        direct_name = button_is_existed.accessible_name
        direct_name = direct_name.replace("검색","")
        return direct_name
    except:
        print("바로검색 불가능")

    
    # 키워드 추출

    test = driver.find_elements(By.CSS_SELECTOR,'div.Vd9M6')
    filter_list = []
    
    for i in test:
        try:
            span = i.find_element(By.CSS_SELECTOR,'span.DdKZJb')
            filter_list.append(i)
        except:
            pass
        
    proudct_name = []
    for i in filter_list:
        try:
            name = i.find_element(By.CSS_SELECTOR,'div.UAiK1e')
            proudct_name.append(name)
        except:
            pass
    
    real_name = []
    for i in proudct_name:
        try:
            real_name.append(i.text)
        except:
            pass
        
    print(real_name)
    
    
    driver.quit()  # WebDriver 종료
    
    return real_name
            
if __name__ == "__main__":
    print("TEST CODE 입니다 ....")
    img_path = "C:/Users/user/Quick_Search/Site_crawling/cap.jpg"  # 이미지경로 TEST PATH
    if os.path.isfile(img_path):
        print("File Exist")
    else:
        print("File Not Exist")
        raise  FileNotFoundError
    keyword = upload_image_and_extract_keyword(img_path) # Site_crawling/target.jpg
    print("keword : ",keyword)