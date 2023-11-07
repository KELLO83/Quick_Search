import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

# UI 파일 로드
ui_file = "GUI.ui"
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
        if self.image_upload_button:
            self.image_upload_button.clicked.connect(self.upload_image)
        else:
            print("Warning: 'image_upload' button not found in the UI form.")

        # 이미지를 표시할 QLabel
        self.image_label = self.findChild(QLabel, 'image')
        if not self.image_label:
            print("Warning: 'image' label not found in the UI form.")

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())
