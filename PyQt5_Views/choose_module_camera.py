from PyQt5 import QtWidgets, uic
import sys
from video_capture import LoadVideo
from camera_capture import CameraVideo

class CameraModule(QtWidgets.QMainWindow):
    def __init__(self):
        super(CameraModule, self).__init__()
        uic.loadUi('ui/camera_module.ui', self)
        self.load_video = LoadVideo()
        self.open_camera = CameraVideo()
        self.button_open_camera = self.findChild(QtWidgets.QPushButton, 'camera') # Find the EditLine
        self.button_load_video = self.findChild(QtWidgets.QPushButton, 'stored') # Find the EditLine
        self.button_open_camera.clicked.connect(self.open_camera_live)
        self.button_load_video.clicked.connect(self.load_video_file)
    
    def open_camera_live(self):
        self.open_camera.show()
    
    def load_video_file(self):
        self.load_video.show()

    

    

