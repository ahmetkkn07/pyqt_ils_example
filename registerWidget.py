from Business.userManager import UserManager
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


class RegisterWidget(QWidget):
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

        label_register = QLabel("Kaydol")
        label_register.setAlignment(QtCore.Qt.AlignCenter)
        label_register.setStyleSheet("font-size: 20px")
        v_box.addWidget(label_register)
        v_box.addStretch()

        h_box_name = QHBoxLayout()
        label_name = QLabel("Ad")
        label_name.setFixedWidth(75)
        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setFixedWidth(200)
        h_box_name.addStretch()
        h_box_name.addWidget(label_name)
        h_box_name.addWidget(self.lineEdit_name)
        h_box_name.addStretch()
        v_box.addLayout(h_box_name)

        h_box_surname = QHBoxLayout()
        label_surname = QLabel("Soyad")
        label_surname.setFixedWidth(75)
        self.lineEdit_surname = QLineEdit()
        self.lineEdit_surname.setFixedWidth(200)
        h_box_surname.addStretch()
        h_box_surname.addWidget(label_surname)
        h_box_surname.addWidget(self.lineEdit_surname)
        h_box_surname.addStretch()
        v_box.addLayout(h_box_surname)

        h_box_username = QHBoxLayout()
        label_username = QLabel("Kullanıcı Adı")
        label_username.setFixedWidth(75)
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setFixedWidth(200)
        h_box_username.addStretch()
        h_box_username.addWidget(label_username)
        h_box_username.addWidget(self.lineEdit_username)
        h_box_username.addStretch()
        v_box.addLayout(h_box_username)

        h_box_password = QHBoxLayout()
        label_password = QLabel("Şifre")
        label_password.setFixedWidth(75)
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.lineEdit_password.setFixedWidth(200)
        self.lineEdit_password.returnPressed.connect(self.login)
        h_box_password.addStretch()
        h_box_password.addWidget(label_password)
        h_box_password.addWidget(self.lineEdit_password)
        h_box_password.addStretch()
        v_box.addLayout(h_box_password)

        h_box_buttons = QHBoxLayout()
        pushButton_register = QPushButton("Kaydol")
        pushButton_register.pressed.connect(self.register)
        pushButton_login = QPushButton("Hesabın var mı? Giriş yap")
        pushButton_login.pressed.connect(self.login)
        h_box_buttons.addStretch()
        h_box_buttons.addWidget(pushButton_login)
        h_box_buttons.addWidget(pushButton_register)
        h_box_buttons.addStretch()

        v_box.addLayout(h_box_buttons)

        v_box.addStretch()

        self.setLayout(v_box)

    def register(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        name = self.lineEdit_name.text().strip()
        surname = self.lineEdit_surname.text().strip()
        try:
            userManager = UserManager()
            userManager.add_user(username, password, name, surname)
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
            msgBox.setText("Kayıt başarılı")
            msgBox.setWindowTitle("Bilgi")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                self.login()

    def login(self):
        from loginWidget import LoginWidget
        self.login = LoginWidget()
        self.login.show()
        self.close()
