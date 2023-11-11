# 실행파일 입니다

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import QUrl



def main():
    sys.path.append("C\\Users\\USER\\Desktop\\Quick_Search") # 본인 실행자의 경로를 추가해주세요
    print("sytem path : ",sys.path)
    from GUI import Ezsearch
    app = QApplication(sys.argv)
    myWindow = Ezsearch.MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
    
    
    


if __name__ == "__main__":
    print("Quick Search 실행합니다....")
    main()
    print("Quick Search 종료합니다....")
    
    
    