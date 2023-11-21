# 실행파일 입니다

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import QUrl
import os

import Controller.detect_controller as d
import Controller.img_controller as i
import Controller.crawl_controller as c

def main():
    sys.path.append(os.getcwd()) 
    from GUI import Ezsearch
    app = QApplication(sys.argv)
    myWindow = Ezsearch.MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
    
    
    


if __name__ == "__main__":
    print("Quick Search 실행합니다....")
    main()
    
    # 이미지 resize 컨트롤러 테스팅 코드
    # i.img_controller.resize_con("./crop_dir")
    
    # 객체탐지 컨트롤러(객체탐지+사용자크롭) 테스팅 코드
    # d.call("Image_process/detect_target.jpg", 'shoes');
    
    # 크롭 테스팅 코드
    #i.img_controller.crop_con("./Image_process/detect_target.jpg", "./label_result/output.txt")
    
    # 이미지 resize 컨트롤러 테스팅 코드 resize 두번 돌려야 비율이 맞음
    #i.img_controller.resize_con("./crop_dir")
    #i.img_controller.resize_con("./crop_dir")

    # 크롤링 테스팅 코드
    #crop_img_path = "C:\\Users\\user\\Quick_Search\\crop_dir\\0.png"
    #prod_info = c.crawling(crop_img_path)

    # i.img_controller.crop_con("./Image_process/detect_target.jpg", "./label_result/output.txt")
    print("Quick Search 종료합니다....")
    
    
