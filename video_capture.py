from PyQt5 import QtWidgets, uic
import sys

class LoadVideo(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoadVideo, self).__init__()
        uic.loadUi('ui/load_video.ui', self)

