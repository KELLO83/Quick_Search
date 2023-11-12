
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import Controller.main_controller
    
    
def get_gui_controller(img_path,category):
    print("이미지 경로  : {} 사용자가 선택한 카테고리 {}".format(img_path,category))
    button = QMessageBox.question(QWidget(), 'Message', '이미지 경로  : {} 사용자가 선택한 카테고리 {}'.format(img_path,category), QMessageBox.Yes)
    
    if button == QMessageBox.Yes:
        print("검색을 시작합니다")
        Controller.main_controller.get_imageinformation(img_path,category)
        
    else:
        print("검색을 취소합니다")
        return False
    
    

    