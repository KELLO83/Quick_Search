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
    
    
    # 키워드 추출
    keyword_list = []
    result = driver.find_elements(By.CSS_SELECTOR,"div.UAiK1e")
    for i in result:
        keyword_list.append(i.text)
        
    keyword_list = [re.sub('[^0-9ㄱ-힗]', '', _) for _ in keyword_list]
    nltk.download('punkt')
    words = []
    for text in keyword_list:
        words.extend(word_tokenize(text))
    words_counts = Counter(words)
    
    most_word = words_counts.most_common(10)
    result = []
    for i in range(most_word.__len__()):
        result.append(most_word[i][0])

    result = [re.sub(r"\d{7}", "", _) for _ in result]
    result = [item for item in result if not item.isdigit()]
               
    print(result)
    driver.quit()  # WebDriver 종료
    return result

if __name__ == "__main__":
    print("TEST CODE 입니다 ....")
    img_path = "C:/Users/user/Quick_Search/Site_crawling/cap.jpg"  # 이미지경로 TEST PATH
    if os.path.isfile(img_path):
        print("File Exist")
    else:
        print("File Not Exist")
        raise  FileNotFoundError
    keyword = upload_image_and_extract_keyword(img_path) # Site_crawling/target.jpg
    # print(keyword)