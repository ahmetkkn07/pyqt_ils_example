from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
    QPushButton,
)
from Alogger import Alogger
logger = Alogger.Alogger(log_level=Alogger.LogLevel.ALL, log_to_file=False)


class MainMenu(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        v_box = QVBoxLayout()

        v_box.addStretch()

        label_program_name = QLabel("Kütüphane Yönetim Sistemi")
        label_program_name.setAlignment(QtCore.Qt.AlignCenter)
        label_program_name.setStyleSheet("font-size: 35px")
        v_box.addWidget(label_program_name)
        v_box.addStretch()

        pushButton_addBook = QPushButton("Kitap Ekle")
        pushButton_addBook.pressed.connect(self.add_book)
        v_box.addWidget(pushButton_addBook)

        pushButton_editBook = QPushButton("Kitap Düzenle")
        pushButton_editBook.pressed.connect(self.edit_book)
        v_box.addWidget(pushButton_editBook)

        pushButton_listBooks = QPushButton("Kitapları Listele")
        pushButton_listBooks.pressed.connect(self.list_books)
        v_box.addWidget(pushButton_listBooks)

        pushButton_logout = QPushButton("Çıkış Yap")
        pushButton_logout.pressed.connect(self.logout)
        v_box.addWidget(pushButton_logout)

        v_box.addStretch()

        self.setLayout(v_box)

    def add_book(self):
        from addBook import AddBook
        self.addBook = AddBook()
        self.addBook.show()
        self.close()

    def edit_book(self):
        pass

    def list_books(self):
        pass

    def logout(self):
        from login import Login
        self.login = Login()
        self.login.show()
        self.close()
