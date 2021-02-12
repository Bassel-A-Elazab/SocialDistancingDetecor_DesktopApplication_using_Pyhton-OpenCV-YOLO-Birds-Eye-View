import cv2

class DecideCameraVideo():
    def __init__(self):
        self.capturing = False
        self.c = None

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
        
    
