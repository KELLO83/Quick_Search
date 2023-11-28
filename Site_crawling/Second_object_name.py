from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
import os


def upload_image_and_extract_keyword(image_path) -> str:
    """ IMAGE_PATH : 이미지 경로를 입력받습니다 안전하게 절대경로로 입력받는것을 권장합니다"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com/")
    
    try:
        lens_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'svg.Gdd5U')))
        lens_icon.click()
    except:
        try:
            lens_icon = driver.find_element(By.CSS_SELECTOR, 'svg.Gdd5U')
            driver.execute_script("""
                        var clickEvent = new MouseEvent("click", {
                            "bubbles": true,
                            "cancelable": true
                        });
                        arguments[0].dispatchEvent(clickEvent);
                    """, lens_icon)
        except:
            try:
                lens_icon =  driver.find_element(By.CSS_SELECTOR, 'svg.Gdd5U')
                actions = ActionChains(driver)
                actions.move_to_element(lens_icon).click().perform()
            except:
                raise super("Image Upload Fail")
            
    time.sleep(1)

    # 파일 입력 요소 선택
    file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
    # WebDriverWait를 사용하여 특정 요소가 로드될 때까지 대기
    time.sleep(1)


    # 이미지 파일의 로컬 경로 지정
    file_input.send_keys(image_path)
    time.sleep(3)
    try:
        button_is_existed = driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/a')
        direct_name = button_is_existed.accessible_name
        direct_name = direct_name.replace("검색","")
        return direct_name
    except:
        print("바로검색 불가능")
    
    
    div_tag = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/c-wiz/div/div[2]/c-wiz/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div/div')
    style = div_tag.get_attribute('style')
    style_dict = dict(item.split(': ') for item in style.split('; ') if item)
    lens_grid_column_count = style_dict.get('--lens-grid-column-count')
    
    elements = driver.find_elements(By.CSS_SELECTOR, 'div.aah4tc > div:nth-child(1) > div.G19kAf.ENn9pd')
    count = len(elements)
    
    elemnts = driver.find_elements(By.CSS_SELECTOR, 'div.aah4tc > div:nth-child(2) > div.G19kAf.ENn9pd')
    count2 = len(elements)
    
    # 키워드 추출
    test = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.Vd9M6'))) #전체 60개
    #test = driver.find_elements(By.CSS_SELECTOR,'div.Vd9M6') 
    new_list = []

    filter_list = []

    #new_list.append(test[0:9])
    #ew_list.append(test[count:count+9])
    
    for i in range(10):
        new_list.append(test[i])
        new_list.append(test[count + i])
            
    for i in new_list:
            try:
                span = i.find_element(By.CSS_SELECTOR,'span.DdKZJb')
                filter_list.append(i) # 60개중에서 상품태그가 붙어있는것만 저장
            except:
                pass
    
    # for i in new_list:
    #     try:
    #         span = i.find_element(By.CSS_SELECTOR,'span.DdKZJb')
    #         filter_list.append(i) # 60개중에서 상품태그가 붙어있는것만 저장
    #     except:
    #         pass
        
    print(filter_list)
        
        
        
    
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
    
    with open("b.txt",'w',encoding='UTF-8') as f:
        for i in real_name:
            f.write(i)
            f.write("\n")

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