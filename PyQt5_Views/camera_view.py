import sys
from os import path

import cv2
import numpy as np

from scipy.spatial import distance as dist

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

    def start_recording(self):                  # for playing video
        self.timer.start(0, self)
        
    def stop_recording(self):                   # for stopping video
        self.timer.stop()
    
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


    def detected_minimum_distance_peoples(self, frame):
        boxes, confidences, centroids = self.extract_detection_informations(frame)
        results = []
        
        # Apply non-maxima suppression to suppress weak, overlapping bounding boxes.
        # Because YOLO doesn't apply it.
        idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence, self.threshold)

        # Check if there is at least one detection exists.
        if len(idxs) > 0:
            for i in idxs.flatten():
                # Extract bounding box coordinates
                x, y = boxes[i][0], boxes[i][1]
                w, h = boxes[i][2], boxes[i][3]
                
                '''
                Assign person detected informations which is:
                    The person probability.
                    The bounding box coordinates,
                    The centroid.
                '''
                r = (confidences[i], (x, y, x + w, y + h), centroids[i])    
                results.append(r)

        violate = set()         # Holds the the set of indexes that violate the minimum social distance.

        # Enter If there are at least two person detections to compute the distance maps.
        if len(results) >= 2:
            centroids = np.array([r[2] for r in results])               # Extract all centroids.
            D = dist.cdist(centroids, centroids, metric="euclidean")    # Computing the Euclidean Distances between all pairs of the centroids.
            
            # loop over the upper triangular of the distance matrix.
            for i in range(0, D.shape[0]):
                for j in range(i+1, D.shape[1]):
                    '''
                    check to see if the distance between any two centroid pairs,
                    is less than the configured number of pixels
                    '''
                    if D[i, j] < self.MIN_DISTANCE:
                        # update out violation set with the indexes of the centroid pairs.
                        violate.add(i)
                        violate.add(j)

        return results, violate
    
    # accept image data from QImage (PyQt5-GUI) from the final results of the detections,
    # Then marked objects with suitable colors.
    def Image_Data_Mark(self, image_data):
        results, violates = self.detected_minimum_distance_peoples(image_data)
        for (i, (prob, bbox, centroid)) in enumerate(results):
            
            (startX, startY, endX, endY) = bbox      # extract the bounding box.
            (cX, cY) = centroid                     # extract the centroid coordinates.
            color = (0, 255, 0)

            # Change the color to red if the index pair exists within the violation set.
            if i in violates:
                color = (0, 0, 255)
                
            cv2.rectangle(image_data, (startX, startY), (endX, endY), color, 2)
            cv2.circle(image_data, (cX, cY), 5, color, 1)

        self.frame = self.get_qimage(image_data)
        if self.frame.size() != self.size():
            self.setFixedSize(self.frame.size())

        self.update()
    
    # Passing the frames from the videos opencv as ndarray and converts to QImage to work within PyQt5-GUI
    def get_qimage(self, image: np.ndarray):
        height, width, colors = image.shape
        bytesPerLine = 3 * width
        QImage = QtGui.QImage

        image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

        image = image.rgbSwapped()
        return image
    
    # For drawing the frames on the PyQt-GUI Window
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.frame)
        self.frame = QtGui.QImage()



