import sys

from PyQt5.QtWidgets import QApplication

from loginWidget import LoginWidget


def main():
    app = QApplication(sys.argv)
    login = LoginWidget()
    login.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
