from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.lineEdit_username = self.findChild(QtWidgets.QLineEdit, 'userName') # Find the EditLine
        self.lineEdit_password = self.findChild(QtWidgets.QLineEdit, 'password') # Find the EditLine
        self.button_login = self.findChild(QtWidgets.QPushButton, 'login') # Find the EditLine
        self.button_login.clicked.connect(self.check_username_password)
        self.show()

    def check_username_password(self):
        msg = QtWidgets.QMessageBox()

        if self.lineEdit_username.text() == 'Bassel' and self.lineEdit_password.text() == '1996':
            msg.setText('Success')
            msg.exec_()
            app.quit()
        else:
            msg.setText('Incorrect Password!!!')
            msg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
