from PyQt5 import QtWidgets, uic
import sys

sys.path.insert(1, 'SocialDistanceProjectOpencv/')
from login import LoginForm

class Home(QtWidgets.QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        uic.loadUi('ui/home.ui', self)
        self.setWindowTitle("Home")
        
        self.Login = LoginForm()
        
        self.button_enter = self.findChild(QtWidgets.QPushButton, 'enter') # Find the Enter button
        self.button_exit = self.findChild(QtWidgets.QPushButton, 'exit') # Find the Exit button

        self.button_enter.clicked.connect(self.open_app)
        self.button_exit.clicked.connect(self.close_app)

    def open_app(self):
        self.close()
        self.Login.show()
    

    def close_app(self):
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Home()
    main.setWindowTitle("Home")
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()