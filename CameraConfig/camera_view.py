import cv2
import sys
import numpy as np

sys.path.insert(1, 'SocialDistanceProjectOpencv/')

from social_detection_model import soical_detect_peoples_using_yolo
from BirdsEyeView import Bird_Eye_View

class DecideCameraVideo():
    def __init__(self):
        self.capturing = False    # To control of video capture.
        self.c = None

        self.image = None         # For marked 6 points  

        self.YOLO_Weights = 'yolo_models/yolov3.weights'
        self.YOLO_Config = 'yolo_models/yolov3.cfg'
        self.CONFIDENCE = 0.5
        self.THRESHOLD = 0.3
        self.MIN_DISTANCE = 50
        
        self.scale_w = 1.2 / 4
        self.scale_h = 4 / 4

        self.mouse_pts = []         

        self.frame_num = 0
        self.first_frame_display = True

        self.color_yellow = (0, 255, 255)

        self.net = cv2.dnn.readNetFromDarknet(self.YOLO_Config, self.YOLO_Weights)
        self.output_layer_names = self.net.getLayerNames()
        self.output_layer_names = [self.output_layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        self.ApplicationDetect = soical_detect_peoples_using_yolo.SoicalDistanceDetectedModel(self.net, self.output_layer_names, self.CONFIDENCE, self.THRESHOLD, self.MIN_DISTANCE)
        self.bird_view = Bird_Eye_View.Top_Down_View()      # For applying a Top-Down View.

    def get_mouse_points(self, event, x, y, flags, param):

        # Used to mark 4 points on the frame zero of the video that will be warped
        # Used to mark 2 points on the frame zero of the video that are 6 feet away
        
        if event == cv2.EVENT_LBUTTONDOWN:
            mouseX, mouseY = x, y
            cv2.circle(self.image, (x, y), 10, (0, 255, 255), 10)
            self.mouse_pts.append((x, y))

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

            self.frame_num += 1
            ret, frame = cap.read()
            if self.frame_num == 1:
                
                cv2.namedWindow("FirstFrame")
                cv2.setMouseCallback("FirstFrame", self.get_mouse_points)
                self.first_frame_display = True
                
                while True:
                    self.image = frame
                    cv2.imshow("FirstFrame", self.image)
                    cv2.waitKey(1)

                    if len(self.mouse_pts) == 7 :
                        cv2.destroyWindow("FirstFrame")
                        break
                    self.first_frame_display = False
            
            if frame is None:
                self.capturing = False
                cv2.destroyAllWindows()
                return 

            detect_result = self.ApplicationDetect.extract_detection_informations(frame)
            M, M_INV, d_thresh = self.bird_view.get_camera_perspective(frame, self.mouse_pts)
            pts = np.array([self.mouse_pts[0], self.mouse_pts[1], self.mouse_pts[3], self.mouse_pts[2]], np.int32)
            cv2.polylines(frame, [pts], True, self.color_yellow, thickness=4)
     
            warped_pts, frame_pts, bird_image = self.bird_view.draw_circle_bird_eye_view(frame, detect_result, M, self.scale_w, self.scale_h)
            frame = self.bird_view.draw_lines_between_nodes(warped_pts, frame_pts, bird_image, frame, d_thresh)
            
            cv2.imshow("Frame", frame)
            cv2.imshow("Bird Eye Views", bird_image)
            cv2.waitKey(1)

        cv2.destroyAllWindows()
        
    def pauseCapture(self):
        if cv2.waitKey(0) & 0xFF == ord('p'):  # Pause
            self.capturing = False

    def endCapture(self):
        self.capturing = False
        self.c = None
        self.frame_num = 0
        self.mouse_pts = []
        self.finish = True
        cv2.destroyAllWindows()
    
    def quitCapture(self):
        cap = self.c
        self.c = None
        cv2.destroyAllWindows()
        
    
