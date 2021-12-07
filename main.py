import sys

from PyQt5.QtWidgets import QApplication

from login import Login


def main():
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
