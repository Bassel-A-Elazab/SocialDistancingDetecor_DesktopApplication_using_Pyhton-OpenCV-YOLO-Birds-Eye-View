from PyQt5 import QtWidgets, uic
import sys

from choose_module_camera import CameraModule     # For deciding whats type of camera modules Live streaming or databases
from check_userName_pass import CheckData

class LoginForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginForm, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.setWindowTitle("Login")
        
        self.Application = CameraModule()
        self.ChangeAccess = CheckData()

        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'userName') # Find the EditLine
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'password') # Find the EditLine

        self.button_login = self.findChild(QtWidgets.QPushButton, 'login') # Find the login button
        self.button_change_access = self.findChild(QtWidgets.QPushButton, 'change') # Find the change user name and password.
        self.button_back_home = self.findChild(QtWidgets.QPushButton, 'back') # Find the change user name and password

        self.button_login.clicked.connect(self.check_username_password)
        self.button_change_access.clicked.connect(self.change_userName_password)
        self.button_back_home.clicked.connect(self.back_home)

    def check_username_password(self):
        msg = QtWidgets.QMessageBox()

        file_data = open("admin_data/login.txt", "r")
        content = file_data.read().split('\n')

        if self.lineEdit_username.text() == content[0] and self.lineEdit_password.text() == content[1]:
            file_data.close()
            self.close()
            self.Application.show()

        else:
            msg.setText('Incorrect userName or Password!!!')
            msg.exec_()

    def change_userName_password(self):
        self.close()    
        self.ChangeAccess.show()

    def back_home(self):
        from home import Home
        self.backHome = Home()
        self.close()
        self.backHome.show()