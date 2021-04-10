import sys

from PyQt5 import QtCore, QtWidgets, QtGui, uic

import cv2
import numpy as np

sys.path.insert(1, 'SocialDistanceProjectOpencv/')
from CameraConfig import camera_view

class LoadVideo(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoadVideo, self).__init__()
        uic.loadUi('ui/load_video.ui', self)

        self.path = ''
        self.YOLO_Weights = 'yolo_models/yolov3.weights'
        self.YOLO_Config = 'yolo_models/yolov3.cfg'
        self.confidence = 0.5
        self.threshold = 0.3
        self.MIN_DISTANCE = 50

        self.ApplicationVideo = camera_view.DecideCameraVideo()

        self.button_open_video = self.findChild(QtWidgets.QPushButton, 'file_open') # Find the open file button
        self.button_start = self.findChild(QtWidgets.QPushButton, 'start')          # Find the start button
        self.button_end = self.findChild(QtWidgets.QPushButton, 'end')              # Find the end button
        self.button_pause = self.findChild(QtWidgets.QPushButton, 'pause')          # Find the pause button
        self.button_quit = self.findChild(QtWidgets.QPushButton, 'quit')            # Find the start button
        self.button_back = self.findChild(QtWidgets.QPushButton, 'back')            # Find the back button
        self.button_logout = self.findChild(QtWidgets.QPushButton, 'logout')        # Find the logout button

        self.button_open_video.clicked.connect(self.upload_video)       # For open a video file
        self.button_start.clicked.connect(self.start_video)             # For start a video
        self.button_end.clicked.connect(self.end_video)                 # For end a video
        self.button_pause.clicked.connect(self.pause_video)             # For pause a video
        self.button_quit.clicked.connect(self.quit_load_video)          # For quit a video
        self.button_back.clicked.connect(self.back_button)              # For back an action
        self.button_logout.clicked.connect(self.logout_app)             # For logout an app

    def upload_video(self):
        self.path = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        if self.path:
            self.ApplicationVideo.setVideoFile(self.path)
    
    def start_video(self):
        if self.path:
            self.ApplicationVideo.startCapture()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText('Sorry! You should choose the video first...')
            msg.exec_()
    
    def pause_video(self):
        self.ApplicationVideo.pauseCapture()
    
    def end_video(self):
        self.ApplicationVideo.endCapture()
    
    def quit_load_video(self):
        from choose_module_camera import CameraModule
        self.ApplicationVideo.endCapture()
        self.Application = CameraModule()
        self.deleteLater()
        self.Application.show()

    def back_button(self):
        from choose_module_camera import CameraModule
        self.Application = CameraModule()
        self.deleteLater()
        self.Application.show()
    
    def logout_app(self):
        self.ApplicationVideo.endCapture()
        from home import Home
        self.backHome = Home()
        self.close()
        self.backHome.show()




