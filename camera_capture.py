from PyQt5 import QtWidgets, uic
import sys

class CameraVideo(QtWidgets.QMainWindow):
    def __init__(self):
        super(CameraVideo, self).__init__()
        uic.loadUi('ui/open_camera.ui', self)
