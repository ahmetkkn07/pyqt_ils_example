from PyQt5.QtGui import QStandardItem, QStandardItemModel
from Business.bookManager import BookManager
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QAbstractItemView,
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


class SelectBookToEditWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        self.setFixedHeight(500)
        self.setFixedWidth(500)

        v_box = QVBoxLayout()

        v_box.addStretch()

        label_title = QLabel("Kitap Düzenle")
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
            # ! Hücre değil satır seçilmesi için
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

            self.itemSelectionModel = self.tableView.selectionModel()

            v_box.addWidget(self.tableView)

            print(books)

        h_box_buttons = QHBoxLayout()
        pushButton_add = QPushButton("Düzenle")
        pushButton_add.pressed.connect(self.edit_book)
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
        from mainMenuWidget import MainMenuWidget
        self.mainMenuWidget = MainMenuWidget()
        self.mainMenuWidget.show()
        self.close()

    def edit_book(self):
        selected_book_id = self.itemSelectionModel.selectedRows()[0].data()
        from editBookWidget import EditBookWidget
        self.editBookWidget = EditBookWidget(selected_book_id)
        self.editBookWidget.show()
        self.close()
