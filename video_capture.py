import sys

from PyQt5 import QtCore, QtWidgets, QtGui, uic

import cv2
import numpy as np

from PyQt5_Views.camera_view import RecordVideo, SoicalDistanceDetectedWidget

class LoadVideo(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoadVideo, self).__init__()
        uic.loadUi('ui/load_video.ui', self)

        self.button_open_video = self.findChild(QtWidgets.QPushButton, 'file_open')
        self.button_start = self.findChild(QtWidgets.QPushButton, 'start') # Find the start button
        self.button_stop = self.findChild(QtWidgets.QPushButton, 'stop') # Find the stop button
        self.button_end = self.findChild(QtWidgets.QPushButton, 'end') # Find the end button
        self.button_pause = self.findChild(QtWidgets.QPushButton, 'pause') # Find the pause button
        self.button_quit = self.findChild(QtWidgets.QPushButton, 'quit') # Find the start button

        self.button_open_video.clicked.connect(self.upload_video)
        
        self.layout = self.findChild(QtWidgets.QVBoxLayout, 'disp_video')

        self.YOLO_Weights = 'yolo_models/yolov3.weights'
        self.YOLO_Config = 'yolo_models/yolov3.cfg'
        self.confidence = 0.5
        self.threshold = 0.3
        self.MIN_DISTANCE = 50
        
        self.net = cv2.dnn.readNetFromDarknet(self.YOLO_Config, self.YOLO_Weights)
        self.output_layer_names = self.net.getLayerNames()
        self.output_layer_names = [self.output_layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        self.social_detection_widget = SoicalDistanceDetectedWidget(self.net, self.output_layer_names, self.confidence, self.threshold, self.MIN_DISTANCE, parent=None)

        self.record_video = RecordVideo()

        Image_Data_Mark = self.social_detection_widget.Image_Data_Mark
        self.record_video.image_data.connect(Image_Data_Mark)

        self.button_start.clicked.connect(self.record_video.start_recording)

        self.layout.addWidget(self.social_detection_widget)


    def upload_video(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self)[0]
        if path:
            self.record_video.setVideoFile(path)
    
def main():
    app = QtWidgets.QApplication(sys.argv)
    main = LoadVideo()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()



