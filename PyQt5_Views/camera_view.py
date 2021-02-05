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

    def extract_detection_informations(self, frame:np.ndarray):
        height, width = frame.shape[:2]

        # Create a blob using opencv-dnn to pass it through the YOLO model.
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)

        '''
            Passing the blob frame to YOLO model,
            Then applying a forward of YOLO object detector.
        '''
        self.net.setInput(blob)
        layer_outputs = self.net.forward(self.output_layer)

        boxes = []              # For holding the detected bounding boxes.
        confidences = []        # For holding the cdetected confidences.
        centroids = []          # For holding the detected centroid of objects.

        for output in layer_outputs:      
        # Iterate over each of the detctions.  
            for detection in output:            
            
                scores = detection[5:]              # Extract the scores of the prediction.
                classID = np.argmax(scores)         # Extract the class ID the prediction.
                conf = scores[classID]              # Extract the scores the confidence of the prediction. 
                
                '''
                First: check for the minimum confidences (i.e., probability) to filter out weak predictions.
                Second: Choose only person in the process of the predictions.
                '''
                if conf > self.confidence and classID == self.personIdx:
                    
                    box = detection[0:4] * np.array([width, height, width, height])     # Scaling the bounding box relative to the size of the image.

                    '''
                    As we know YOLO return the center (x, y) coordinates of the bounding box, 
                    Then the boxes width and height.
                    '''
                    centerX, centerY, w, h = box.astype('int')                          

                    # Use the center coordinates, width and height to get the coordinates of the top left corner.
                    x = int(centerX - (w / 2))
                    y = int(centerY - (h / 2))

                    # Append All of the essentail information of detected [bounding boxes, confidences, centroids]
                    boxes.append([x, y, int(w), int(h)])
                    confidences.append(float(conf))
                    centroids.append((centerX, centerY))
                
        return boxes, confidences, centroids     


        


