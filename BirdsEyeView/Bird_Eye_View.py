from PyQt5 import QtWidgets, uic
import sys

sys.path.insert(1, 'SocialDistanceProjectOpencv/')

from choose_module_camera import CameraModule     # For deciding whats type of camera modules Live streaming or databases

class LoginForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginForm, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.Application = CameraModule()
        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'userName') # Find the EditLine
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'password') # Find the EditLine
        self.button_login = self.findChild(QtWidgets.QPushButton, 'login') # Find the login button
        self.button_login.clicked.connect(self.check_username_password)
        
    def check_username_password(self):
        msg = QtWidgets.QMessageBox()

        if self.lineEdit_username.text() == 'Sara' and self.lineEdit_password.text() == '1996':
            self.close()
            self.deleteLater()
            self.Application.show()

        else:
            msg.setText('Incorrect Password!!!')
            msg.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = LoginForm()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()

