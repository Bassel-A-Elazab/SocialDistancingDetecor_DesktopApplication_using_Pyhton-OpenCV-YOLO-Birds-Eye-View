from PyQt5 import QtWidgets, uic
import sys
from PyQt5_Views.camera_view import MainWidget     # Importing the camera view and the system detection.
class LoginForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginForm, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.Application = MainWidget('yolo_models/yolov3.cfg', 'yolo_models/yolov3.weights', 0.5, 0.3, 50)
        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'userName') # Find the EditLine
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'password') # Find the EditLine
        self.button_login = self.findChild(QtWidgets.QPushButton, 'login') # Find the EditLine
        self.button_login.clicked.connect(self.check_username_password)
        

    def check_username_password(self):
        msg = QtWidgets.QMessageBox()

        if self.lineEdit_username.text() == 'Bassel' and self.lineEdit_password.text() == '1996':
            self.close()
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

