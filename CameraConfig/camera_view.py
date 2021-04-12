import cv2
import sys

sys.path.insert(1, 'SocialDistanceProjectOpencv/')

from social_detection_model import soical_detect_peoples_using_yolo
from BirdsEyeView import Bird_Eye_View

class DecideCameraVideo():
    def __init__(self):
        self.capturing = False
        self.c = None

        self.YOLO_Weights = 'yolo_models/yolov3.weights'
        self.YOLO_Config = 'yolo_models/yolov3.cfg'
        self.CONFIDENCE = 0.5
        self.THRESHOLD = 0.3
        self.MIN_DISTANCE = 50
        
        self.net = cv2.dnn.readNetFromDarknet(self.YOLO_Config, self.YOLO_Weights)
        self.output_layer_names = self.net.getLayerNames()
        self.output_layer_names = [self.output_layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        self.ApplicationDetect = soical_detect_peoples_using_yolo.SoicalDistanceDetectedModel(self.net, self.output_layer_names, self.CONFIDENCE, self.THRESHOLD, self.MIN_DISTANCE)
    def setCameraPort(self):
        if self.c is not None:
            cv2.destroyAllWindows()
            self.c.release()
        self.c = cv2.VideoCapture(0)
    
    def setVideoFile(self, path):
        if self.c is not None:
            cv2.destroyAllWindows()
            self.c.release()
        self.c = cv2.VideoCapture(path)
    
    def startCapture(self):
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()
            if frame is None:
                self.capturing = False
                cv2.destroyAllWindows()
                return 
            cv2.imshow("Frame", frame)
            self.ApplicationDetect.Image_Data_Mark(frame)
            cv2.waitKey(5)
        cv2.destroyAllWindows()
        
    def pauseCapture(self):
        if cv2.waitKey(0) & 0xFF == ord('p'):  # Pause
            self.capturing = False

    def endCapture(self):
        self.capturing = False
        self.c = None
        cv2.destroyAllWindows()
    
    def quitCapture(self):
        cap = self.c
        self.c = None
        cv2.destroyAllWindows()
        
    
