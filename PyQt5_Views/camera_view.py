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
        read, frame = self.cameera.read()
        if read:
            self.image_data.emit(frame)
    


