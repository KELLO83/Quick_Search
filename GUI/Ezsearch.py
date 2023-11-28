import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTextBrowser
import Controller.gui_controller
import sqlite3

# UI 파일 로드
ui_file = "GUI/GUI2.ui"
Ui_Form, QtBaseClass = uic.loadUiType(ui_file)
     
# Class 생성
class MyWindow(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 데이터베이스 연결 
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("EzSearch.db")

        if not self.db.open():
            QMessageBox.critical(self, "에러", "데이터베이스 연결 오류", QMessageBox.Ok)
            sys.exit(1)

        # 데이터베이스에서 불러온 데이터를 저장할 객체 
        self.database_data = None

        # 데이터베이스에서 데이터 불러오기 
        self.load_data_from_database()    

        # 이미지 
        self.image = self.findChild(QLabel, 'image')

        # 상품명 
        self.Pname = self.findChild(QTextBrowser, 'Pname')

        # 가격 
        self.Pprice = self.findChild(QTextBrowser, 'Pprice')

        # 데이터베이스에서 데이터 불러오기 
    def load_data_from_database(self):
        query = QSqlQuery("SELECT seq, category, name, price, purchase_url FROM Ezsearch", self.db)

        # 데이터를 리스트로 저장
        self.database_data = [list(query.record()) for _ in range(query.size())]

        # 데이터 출력
        self.display_data_from_database()

    # 데이터를 UI에 출력
    def display_data_from_database(self):
        # 데이터를 출력할 테이블 모델 생성
        table_model = QSqlTableModel(self)
        table_model.setTable("Ezsearch")  # 테이블 이름 설정
        table_model.setEditStrategy(QSqlTableModel.OnFieldChange)
        table_model.select()

        # 테이블 위젯에 모델 설정
        self.database.setColumnCount(table_model.columnCount())
        self.database.setRowCount(table_model.rowCount())

        # 행 헤더 숨기기
        self.database.verticalHeader().setVisible(False)

        # 각 열의 너비를 설정
        self.database.setColumnWidth(0, 20)  # 번호 열의 너비를 20으로 설정
        self.database.setColumnWidth(1, 50)  # 카테고리의 열의너비를 50으로 설정
        self.database.setColumnWidth(2, 250)  # 상품명 열의 너비를 250으로 설정
        self.database.setColumnWidth(3, 110)  # 가격 열의 너비를 110으로 설정
        self.database.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # 수평 스크롤바 비활성화

        # 데이터베이스 데이터 초기화
        self.database_data = []

        for row in range(table_model.rowCount()):
            row_data = [str(table_model.index(row, col).data()) for col in range(table_model.columnCount())]

            # 데이터를 database_data에 추가
            self.database_data.append(row_data)

            for col in range(table_model.columnCount()):
                item = QTableWidgetItem(row_data[col])

                # 셀을 편집하지 못하도록 설정
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                self.database.setItem(row, col, item)

        # 테이블 위젯의 itemClicked 시그널에 슬롯을 연결
        self.database.itemClicked.connect(self.show_selected_data)

    # 테이블 위젯의 특정 셀이 클릭되었을 때 호출될 슬롯
    def show_selected_data(self, item):
        # item 변수를 통해 클릭된 셀의 정보에 접근 가능
        row = item.row()
        col = item.column()

        # 데이터베이스에서 해당 행의 데이터 가져오기
        if row < len(self.database_data):
            seq = self.database_data[row][0]
            category = self.database_data[row][1]
            name = self.database_data[row][2]
            price = self.database_data[row][3]
            purchase_url = self.database_data[row][4]  # purchase_url 가져오기

            # 해당 데이터를 출력할 QTextBrowser에 설정
            Pname_text_browser = self.findChild(QTextBrowser, 'Pname')
            Pprice_text_browser = self.findChild(QTextBrowser, 'Pprice')

            if Pname_text_browser is not None:
                Pname_text_browser.clear()  # 기존 텍스트 지우기
                Pname_text_browser.append(name)  # 상품명 갱신
                Pname_text_browser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 수직 스크롤 바 비활성화
                Pname_text_browser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 수평 스크롤 바 비활성화
                font = QFont()
                font.setPointSize(10)  # 텍스트 크기 조절
                Pname_text_browser.setFont(font)

            if Pprice_text_browser is not None:
                Pprice_text_browser.clear()  # 기존 텍스트 지우기
                Pprice_text_browser.append(price)  # 가격 갱신
                Pprice_text_browser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 수직 스크롤 바 비활성화
                Pprice_text_browser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # 수평 스크롤 바 비활성화

            # 이미지 로딩
            self.load_image_from_url(QUrl(purchase_url))
        def add_data_to_database(self):
            # 데이터베이스에 데이터 추가
            conn = sqlite3.connect('EzSearch.db')
            cursor = conn.cursor()

            category = self.category_combobox.currentText()
            name = self.Pname.toPlainText()
            price = self.Pprice.toPlainText()
            purchase_url = [item[4] for item in self.database_data]

            cursor.execute("INSERT INTO tem (category, name, price, purchase_url) VALUES (?, ?, ?, ?)",
                   (category, name, price, purchase_url))

            # 변경사항 저장 및 연결 종료
            conn.commit()
            conn.close()

            # 추가한 데이터를 데이터베이스에서 다시 불러오기
            self.load_data_from_database()


        # 'exit_button' 찾기
        self.exit_button = self.findChild(QPushButton, 'exit_button')
        self.exit_button.clicked.connect(self.close_application)

        # 'exit_button'이 정의되었는지 확인 후 이벤트 연결
        if self.exit_button:
            self.exit_button.clicked.connect(self.exit_sys)
        else:
            print("Warning: 'exit_button' not found in the UI form.")

        # 이미지 업로드 버튼 이벤트 연결
        self.image_upload_button = self.findChild(QPushButton, 'image_upload')
        self.image_upload_button.clicked.connect(self.upload_image)

        # 네트워크 엑세스
        self.manager = QNetworkAccessManager()
       

        # 이미지를 표시할 QLabel
        self.image_label = self.findChild(QLabel, 'image')

        # 이미지 파일 경로를 저장할 변수
        self.image_path = ""

        # 파일 디렉터리 패스 
        self.test2_label = self.findChild(QLabel, 'test2')
        
        # Category ComboBox
        self.category_combobox = self.findChild(QComboBox, 'category')
        self.category_combobox.addItem('None')
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

    # 애플리케이션 종료 이벤트 처리
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        

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
        # self.load_image_from_url(self.image_url)
        
        if self.category_combobox.currentText() == 'None':
            QMessageBox.about(self, "카테고리 선택", "카테고리를 선택하세요")
            print("카테고리를 선택하세요")
            return False
        if self.image_path == "":
            QMessageBox.about(self, "이미지 업로드", "이미지를 업로드 하세요")
            print("이미지를 업로드 하세요")
            return False
        
        flag = Controller.gui_controller.get_gui_controller(self.image_path,self.category) #GUI 컨틀롤러 호출 <송준현>
        
        # 컨트롤러를 호출하여 정보를 가져오기 (실제 컨트롤러에 따라 이 부분을 수정해야 할 수 있음)
        flag = Controller.gui_controller.get_gui_controller(self.image_path, self.category) 

        # 컨트롤러가 True를 반환하면 데이터를 데이터베이스에 추가
        if flag:
            self.add_data_to_database()
    # 데이터베이스에 데이터 추가
    def add_data_to_database(self):
        conn = sqlite3.connect('EzSearch.db')
        cursor = conn.cursor()

        category = self.category_combobox.currentText()
        name = self.Pname.toPlainText()
        price = self.Pprice.toPlainText()
        purchase_url = [item[4] for item in self.database_data]

        cursor.execute("INSERT INTO tem (category, name, price, purchase_url) VALUES (?, ?, ?, ?)",
                       (category, name, price, purchase_url))

        # 변경사항 저장 및 연결 종료
        conn.commit()
        conn.close()

        # 추가한 데이터를 데이터베이스에서 다시 불러오기
        self.load_data_from_database()

    # ========== Category 업데이트 ==========
    def update_category(self):
        selected_category = self.category_combobox.currentText()

        # if-elif-else 문을 사용하여 Category에 따라 분류
        
        # names: ['long-pants', 'long-sleeve', 'short-pants', 'short-sleeve', 'sleeveless'] ---> 상하의 인공지능이 구별하는것.. <메모>
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