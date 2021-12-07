from Business.bookManager import BookManager
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QPushButton,
    QMessageBox
)
from Alogger import Alogger
logger = Alogger.Alogger(log_level=Alogger.LogLevel.ALL, log_to_file=False)


class AddBookWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        v_box = QVBoxLayout()

        v_box.addStretch()

        label_title = QLabel("Kitap Ekle")
        label_title.setAlignment(QtCore.Qt.AlignCenter)
        label_title.setStyleSheet("font-size: 20px")
        v_box.addWidget(label_title)
        v_box.addStretch()

        h_box_book_name = QHBoxLayout()
        label_book_name = QLabel("Kitap Adı")
        label_book_name.setFixedWidth(75)
        self.lineEdit_book_name = QLineEdit()
        self.lineEdit_book_name.setFixedWidth(200)
        h_box_book_name.addStretch()
        h_box_book_name.addWidget(label_book_name)
        h_box_book_name.addWidget(self.lineEdit_book_name)
        h_box_book_name.addStretch()
        v_box.addLayout(h_box_book_name)

        h_box_author = QHBoxLayout()
        label_author = QLabel("Yazar")
        label_author.setFixedWidth(75)
        self.lineEdit_author = QLineEdit()
        self.lineEdit_author.setFixedWidth(200)
        h_box_author.addStretch()
        h_box_author.addWidget(label_author)
        h_box_author.addWidget(self.lineEdit_author)
        h_box_author.addStretch()
        v_box.addLayout(h_box_author)

        h_box_number_of_pages = QHBoxLayout()
        label_number_of_pages = QLabel("Sayfa Sayısı")
        label_number_of_pages.setFixedWidth(75)
        self.lineEdit_number_of_pages = QLineEdit()
        self.lineEdit_number_of_pages.setFixedWidth(200)
        h_box_number_of_pages.addStretch()
        h_box_number_of_pages.addWidget(label_number_of_pages)
        h_box_number_of_pages.addWidget(self.lineEdit_number_of_pages)
        h_box_number_of_pages.addStretch()
        v_box.addLayout(h_box_number_of_pages)

        h_box_publisher = QHBoxLayout()
        label_publisher = QLabel("Yayınevi")
        label_publisher.setFixedWidth(75)
        self.lineEdit_publisher = QLineEdit()
        self.lineEdit_publisher.setFixedWidth(200)
        self.lineEdit_publisher.returnPressed.connect(self.add)
        h_box_publisher.addStretch()
        h_box_publisher.addWidget(label_publisher)
        h_box_publisher.addWidget(self.lineEdit_publisher)
        h_box_publisher.addStretch()
        v_box.addLayout(h_box_publisher)

        h_box_buttons = QHBoxLayout()
        pushButton_add = QPushButton("Ekle")
        pushButton_add.pressed.connect(self.add)
        pushButton_back = QPushButton("Geri Dön (İptal)")
        pushButton_back.pressed.connect(self.main_menu)
        h_box_buttons.addStretch()
        h_box_buttons.addWidget(pushButton_back)
        h_box_buttons.addWidget(pushButton_add)
        h_box_buttons.addStretch()

        v_box.addLayout(h_box_buttons)

        v_box.addStretch()

        self.setLayout(v_box)

    def add(self):
        name = self.lineEdit_book_name.text().strip()
        author = self.lineEdit_author.text().strip()
        number_of_pages = self.lineEdit_number_of_pages.text().strip()
        publisher = self.lineEdit_publisher.text().strip()
        try:
            bookManager = BookManager()
            bookManager.add_book(name, author, number_of_pages, publisher)
        except Exception as exception:
            logger.error(exception)
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Veri tabanı hatası!")
            msgBox.setWindowTitle("Hata")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                pass
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("İşlem başarılı")
            msgBox.setWindowTitle("Bilgi")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                pass

    def main_menu(self):
        from mainMenuWidget import MainMenuWidget
        self.mainMenu = MainMenuWidget()
        self.mainMenu.show()
        self.close()
