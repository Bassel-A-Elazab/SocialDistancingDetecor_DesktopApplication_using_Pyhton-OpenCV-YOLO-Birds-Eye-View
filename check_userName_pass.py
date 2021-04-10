from PyQt5 import QtWidgets, uic
import sys

from change_userName_pass import ChangeData

class CheckData(QtWidgets.QMainWindow):
    def __init__(self):

        super(CheckData, self).__init__()
        uic.loadUi('ui/access_old.ui', self)

        self.changeData = ChangeData()

        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'old_name') # Find the EditLine
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'old_pass') # Find the EditLine

        self.button_change = self.findChild(QtWidgets.QPushButton, 'sure_old') # Find the Submit button
        self.button_back_login = self.findChild(QtWidgets.QPushButton, 'back') # Find the Back button

        self.button_change.clicked.connect(self.check_username_password)
        self.button_back_login.clicked.connect(self.back_login)


    def check_username_password(self):
        msg = QtWidgets.QMessageBox()
        file_data = open("admin_data/login.txt", "r")
        content = file_data.read().split('\n')

        if self.lineEdit_username.text() == content[0] and self.lineEdit_password.text() == content[1]:
            file_data.close()
            self.close()
            self.changeData.show()

        else:
            msg.setText('Incorrect UserName Or Password!!!')
            msg.exec_()

    def back_login(self):
        from login import LoginForm
        self.Login = LoginForm()
        self.close()
        self.Login.show()


