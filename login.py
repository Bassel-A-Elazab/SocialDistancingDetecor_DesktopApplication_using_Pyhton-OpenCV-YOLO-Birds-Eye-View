from PyQt5 import QtWidgets, uic
import sys

sys.path.insert(1, 'SocialDistanceProjectOpencv/')

from choose_module_camera import CameraModule     # For deciding whats type of camera modules Live streaming or databases
from change_userName_pass import ChangeData

class LoginForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginForm, self).__init__()
        uic.loadUi('ui/login.ui', self)

        self.Application = CameraModule()

        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'userName') # Find the EditLine
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'password') # Find the EditLine

        self.button_login = self.findChild(QtWidgets.QPushButton, 'login') # Find the login button
	    self.button_change_access = self.findChild(QtWidgets.QPushButton, 'change') # Find the change user name and password

        self.button_login.clicked.connect(self.check_username_password)
	    self.button_change_access.clicked.connect(self.change_userName_password)
        
    def check_username_password(self):
        msg = QtWidgets.QMessageBox()

        if self.lineEdit_username.text() == 'Sara' and self.lineEdit_password.text() == '1996':
            self.close()
            self.deleteLater()
            self.Application.show()

        else:
            msg.setText('Incorrect Password!!!')
            msg.exec_()

	def change_userName_password(self):
        self.close()
        self.ChangeAccess.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = LoginForm()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()

