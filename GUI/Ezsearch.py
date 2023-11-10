import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import QUrl

# UI 파일 로드
ui_file = "GUI2.ui"
Ui_Form, QtBaseClass = uic.loadUiType(ui_file)
     
# Class 생성
class MyWindow(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 'exit_button' 찾기
        self.exit_button = self.findChild(QPushButton, 'exit_button')

        # 'exit_button'이 정의되었는지 확인 후 이벤트 연결
        if self.exit_button:
            self.exit_button.clicked.connect(self.exit_sys)
        else:
            print("Warning: 'exit_button' not found in the UI form.")

        # 이미지 업로드 버튼 이벤트 연결
        self.image_upload_button = self.findChild(QPushButton, 'image_upload')
        self.image_upload_button.clicked.connect(self.upload_image)
       

        # 이미지를 표시할 QLabel
        self.image_label = self.findChild(QLabel, 'image')

        # 이미지 파일 경로를 저장할 변수
        self.image_path = ""

        # 파일 디렉터리 패스 
        self.test2_label = self.findChild(QLabel, 'test2')
        
        # Category ComboBox
        self.category_combobox = self.findChild(QComboBox, 'category')
        self.category_combobox.currentIndexChanged.connect(self.update_category)

        # QLabel for displaying category
        self.test1_label = self.findChild(QLabel, 'test1')
       
        # 이미지 URL을 저장할 변수
        self.image_url = QUrl("https://cdn.011st.com/11dims/resize/320/11src/dl/v2/3/7/5/5/4/6/bTGgM/3053375546_150614628_05.jpg")

        # QPushButton for searching
        self.search_button = self.findChild(QPushButton, 'search_button')
        if self.search_button:
            self.search_button.clicked.connect(self.search_image)
        
        # QNetworkAccessManager
        self.manager = QNetworkAccessManager()

    # ========== 시스템 종료 ==========
    def exit_sys(self):
        exit_msg = "프로그램을 종료 하겠습니까?"
        ans = QMessageBox.question(self, "프로그램 종료", exit_msg, QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.Yes:
            self.close()

    # ========== 이미지 업로드 ==========
    def upload_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, '이미지 업로드', '', 'Image Files (*.png *.jpg *.bmp)')
        if fname:
            pixmap = QPixmap(fname)
            self.image_label.setPixmap(pixmap)
            self.image_path = fname
            self.test2_label.setText(self.image_path)

    # ========== 이미지 URL에서 이미지 로드 ==========
    def load_image_from_url(self, url):
        request = QNetworkRequest(url)
        reply = self.manager.get(request)

        reply.finished.connect(lambda: self.on_image_load_finished(reply))

    # ========== 이미지 로드 완료 후 처리 ==========
    def on_image_load_finished(self, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.image_label.setPixmap(pixmap)
        else:
            print("Error loading image:", reply.errorString())

    # ========== 이미지 검색 ==========
    def search_image(self):
        # 검색 버튼을 눌렀을 때 이미지 URL을 이용하여 이미지를 로드
        self.load_image_from_url(self.image_url)

    # ========== Category 업데이트 ==========
    def update_category(self):
        selected_category = self.category_combobox.currentText()

        # if-elif-else 문을 사용하여 Category에 따라 분류
        if selected_category == '신발':
            self.category = 'shoes'
        elif selected_category == '상의':
            self.category = 'top'
        elif selected_category == '하의':
            self.category = 'bottom'
        elif selected_category == '모자':
            self.category = 'cap'
        else:
            self.category = 'unknown'

        self.test1_label.setText(self.category)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
