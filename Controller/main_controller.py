import Controller.detect_controller as det
import copy
import Controller.img_controller 
import crawl_controller as crawl
import os
import sqlite3

name =[]
price = []
purchase_url = []
image_url = []


def get_imageinformation(img_path,category):
    """ GUI 로부터 선택한 사진의 경로와 카테고리를 받아옵니다. """
    # names: ['long-pants', 'long-sleeve', 'short-pants', 'short-sleeve', 'sleeveless'] ---> 상하의 인공지능이 구별하는것.. <메모>
    top = ['long-sleeve','short-sleeve','sleeveless']
    bottom = ['long-pants','short-pants']
    
    target = None
    
    if category == "top":
        target = copy.deepcopy(top)
    elif category == "bottom":
        target = copy.deepcopy(bottom)
        
    print(f"detect_controller 전달전 검사.. 실행 사진경로 {img_path} 사용자 검색 카테고리 {target}")
    det.call(img_path,target)
    
    image_preprocessing(img_path)

def image_preprocessing(img_path):
    preprocess = Controller.img_controller.img_controller(img_path , "./crop_dir/","./label_result/output.txt")
    preprocess.resize_con()
    preprocess.crop_con()
    print("이미지 전처리 완료")

def crawling():
    for crop_img in os.listdir("./crop_dir"):
        img_path = "./crop_dir/" +  crop_img

        name_list = crawl.crawl_objectname(img_path)
        info = crawl.crawl_sitename(name_list)
    
        name.append(info['product_name'])
        price.append(info['price'])
        purchase_url.append(info['link'])
        image_url.append(info['imgurl'])


if __name__ == "__main__":
    import sys
    sys.path.append("C:/Users/user/Quick_Search")
    
    print(sys.path)
    import Controller.detect_controller as det
    import copy
    import Controller.img_controller 

    image_preprocessing("Image_process/detect_target.jpg")

    
    """sys.path.append(os.getcwd()) 
    from GUI import Ezsearch
    app = QApplication(sys.argv)
    myWindow = Ezsearch.MyWindow()
    myWindow.show()
    sys.exit(app.exec_())"""

