from PyQt5 import QtWidgets, uic
import sys

class ChangeData(QtWidgets.QMainWindow):
    def __init__(self):

        super(ChangeData, self).__init__()
        uic.loadUi('ui/access_new.ui', self)
        
        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'new_name') # Find the EditLine
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'new_pass') # Find the EditLine

        self.button_login = self.findChild(QtWidgets.QPushButton, 'change_confirm') # Find the Confirm button
        self.button_back_login = self.findChild(QtWidgets.QPushButton, 'back') # Find the Back button

        self.button_login.clicked.connect(self.change_username_password)
        self.button_back_login.clicked.connect(self.back_login)

    def change_username_password(self):
        msg = QtWidgets.QMessageBox()
    
        if self.lineEdit_username.text() != "" and self.lineEdit_password.text() != "":
            file_data = open("login.txt", "w")
            file_data.write(self.lineEdit_username.text()+"\n")
            file_data.write(self.lineEdit_password.text())
            file_data.close()
            from login import LoginForm
            self.loginWindow = LoginForm()
            self.close()
            self.loginWindow.show()
        else:
            msg.setText('Empty UserName Or Password!!!')
            msg.exec_()
        
    def back_login(self):
        from login import LoginForm
        self.Login = LoginForm()
        self.close()
        self.Login.show()
    
