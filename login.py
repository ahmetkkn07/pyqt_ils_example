from Business.UserManager import UserManager
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


class Login(QWidget):
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
        pushButton_login = QPushButton("Giriş Yap")
        pushButton_login.pressed.connect(self.login)
        pushButton_register = QPushButton("Hesabın yok mu? Kaydol")
        pushButton_register.pressed.connect(self.register)
        h_box_buttons.addStretch()
        h_box_buttons.addWidget(pushButton_register)
        h_box_buttons.addWidget(pushButton_login)
        h_box_buttons.addStretch()

        v_box.addLayout(h_box_buttons)

        v_box.addStretch()

        self.setLayout(v_box)

    def login(self):
        username = self.lineEdit_username.text().strip()
        password = self.lineEdit_password.text().strip()
        try:
            userManager = UserManager()
            user = userManager.get_user(username, password)
            if user is None:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Kullanıcı adı veya şifre hatalı!")
                msgBox.setWindowTitle("Hata")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    pass
            else:
                print("GİRİŞ BAŞARILI", user)
                self.main_menu()
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

    def register(self):
        from register import Register
        self.register = Register()
        self.register.show()
        self.close()

    def main_menu(self):
        from mainMenu import MainMenu
        self.mainMenu = MainMenu()
        self.mainMenu.show()
        self.close()
