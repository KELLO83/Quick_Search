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

def main():
    sys.path.append(os.getcwd()) 
    from GUI import Ezsearch
    app = QApplication(sys.argv)
    myWindow = Ezsearch.MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
    
    
    


if __name__ == "__main__":
    print("Quick Search 실행합니다....")
    #main()
    #d.call("Image_process/detect_target.jpg", 'shoes')
    i.img_controller.resize_con("./crop_dir")
    print("Quick Search 종료합니다....")
    
    
    