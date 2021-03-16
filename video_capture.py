import sys

from PyQt5 import QtCore, QtWidgets, QtGui, uic

import cv2
import numpy as np

from CameraConfig import camera_view

class LoadVideo(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoadVideo, self).__init__()
        uic.loadUi('../ui/load_video.ui', self)

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
        self.button_quit = self.findChild(QtWidgets.QPushButton, 'back') # Find the back button

        self.button_open_video.clicked.connect(self.upload_video)       # For open a video file
        self.button_start.clicked.connect(self.start_video)             # For start a video
        self.button_end.clicked.connect(self.end_video)                 # For end a video
        self.button_pause.clicked.connect(self.pause_video)             # For pause a video
        self.button_quit.clicked.connect(self.quit_load_video)          # For quit a video


    def upload_video(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        if path:
            self.ApplicationVideo.setVideoFile(path)
    
    def start_video(self):
        self.ApplicationVideo.startCapture()
    
    def pause_video(self):
        self.ApplicationVideo.pauseCapture()
    
    def end_video(self):
        self.ApplicationVideo.endCapture()
    
    def quit_load_video(self):
        self.ApplicationVideo.quitCapture()
        self.close()

    def back_button(self):
        self.deleteLater()
    
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = LoadVideo()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()



