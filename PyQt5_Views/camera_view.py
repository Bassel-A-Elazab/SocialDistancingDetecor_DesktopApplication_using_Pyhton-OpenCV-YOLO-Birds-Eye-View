import sys
from os import path

import cv2
import numpy as np

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

# Establish the reading process of the video stream/stored
class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_path_port, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_path_port)
        self.timer = QtCore.QBasicTimer()
    def start_recording(self):
        self.timer.start(0, self)

    def timerEvent(self, event):
        if(event.timerId() != self.timer.timerId()):
            return
        read, frame = self.camera.read()
        if read:
            self.image_data.emit(frame)


class SoicalDistanceDetectedWidget(QtWidgets.QWidget):

    #Initalize the important arguments for predictions.
    def __init__(self, net_yolo, output_layer_names, arg_confidence, arg_threshold, min_distance, parent=None):
        super().__init__(parent)
        self.frame = QtGui.QImage()
        self.net = net_yolo
        self.output_layer = output_layer_names
        self.confidence = arg_confidence
        self.threshold = arg_threshold
        self.MIN_DISTANCE = min_distance
        self.personIdx = 0

            


        


