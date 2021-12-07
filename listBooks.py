from PyQt5.QtGui import QStandardItem, QStandardItemModel
from Business.bookManager import BookManager
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QVBoxLayout,
    QWidget,
    QTableView,
    QPushButton,
    QMessageBox
)
from Alogger import Alogger
logger = Alogger.Alogger(log_level=Alogger.LogLevel.ALL, log_to_file=False)


class ListBooks(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        v_box = QVBoxLayout()

        v_box.addStretch()

        label_title = QLabel("Kitap Listele")
        label_title.setAlignment(QtCore.Qt.AlignCenter)
        label_title.setStyleSheet("font-size: 20px")
        v_box.addWidget(label_title)
        v_box.addStretch()

        try:
            bookManager = BookManager()
            books = bookManager.get_all()
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
            self.tableView = QTableView()

            # self.model = TableModel(books)
            self.standardItemModel = QStandardItemModel()
            for row, book in enumerate(books):

                for column, data in enumerate(book):
                    item = QStandardItem(str(data))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.standardItemModel.setItem(row, column, item)

            self.standardItemModel.setHorizontalHeaderLabels(
                ["Id", "Kitap Adı", "Yazar", "Sayfa Sayısı", "Yayınevi"])
            self.tableView.setModel(self.standardItemModel)

            # ! Dikey sütun sayılarını gizle
            self.tableView.verticalHeader().hide()
            # ! Hücre genişliklerini ortala
            self.tableView.horizontalHeader().setSectionResizeMode(
                QHeaderView.Stretch)
            self.tableView.setMinimumHeight(300)
            v_box.addWidget(self.tableView)

            print(books)

        h_box_buttons = QHBoxLayout()
        pushButton_add = QPushButton("Boş")
        # pushButton_add.pressed.connect(self.add)
        pushButton_back = QPushButton("Geri Dön")
        pushButton_back.pressed.connect(self.main_menu)
        h_box_buttons.addStretch()
        h_box_buttons.addWidget(pushButton_back)
        h_box_buttons.addWidget(pushButton_add)
        h_box_buttons.addStretch()

        v_box.addLayout(h_box_buttons)

        v_box.addStretch()

        self.setLayout(v_box)

    def main_menu(self):
        from mainMenu import MainMenu
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.close()
