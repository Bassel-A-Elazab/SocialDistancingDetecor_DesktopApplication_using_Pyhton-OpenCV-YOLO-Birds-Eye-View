import numpy as np 
import argparse
import cv2
import os
import time
from scipy.spatial import distance as dist


'''
Passes the arguments in terminal to run the models where is consists of :
    1- wieghts --> YOLO model weights
    2- config --> YOLO model configuration
    3- labels --> YOLO model names
    4- confidence --> The minimum confidence (probability) to avoid weak detected
    5- threshold --> The value of threshold that is used in Non-Maximum suppersion
    6- use_gpu --> If you are use the gpu of compilation process
    7- save --> If you want to save the output results
    8- show --> If you want to show the frames
    9- image_path --> Passing an image to test

'''
parser = argparse.ArgumentParser()
parser.add_argument('-w', '--weights', type=str, default='model/yolov3.weights', help='Path to model weights')
parser.add_argument('-cfg', '--config', type=str, default='model/yolov3.cfg', help='Path to configuration file')
parser.add_argument('-l', '--labels', type=str, default='model/coco.names', help='Path to label file')
parser.add_argument('-c', '--confidence', type=float, default=0.5, help='Minimum confidence for a box to be detected.')
parser.add_argument('-t', '--threshold', type=float, default=0.3, help='Threshold for Non-Max Suppression')
parser.add_argument('-u', '--use_gpu', default=False, action='store_true', help='Use GPU (OpenCV must be compiled for GPU). For more info checkout: https://www.pyimagesearch.com/2020/02/03/how-to-use-opencvs-dnn-module-with-nvidia-gpus-cuda-and-cudnn/')
parser.add_argument('-s', '--save', default=False, action='store_true', help='Whether or not the output should be saved')
parser.add_argument('-sh', '--show', default=True, action="store_false", help='Show output')
parser.add_argument('-i', '--image_path', type=str, default='', help='Path to the image file.')
args = parser.parse_args()

personIdx = 0           # Used in YOLO for detection only persons.
MIN_DISTANCE = 50       # Set the minimum distance initially between two persons.

'''
    Using YOLO v3 model to detect only people from image.
    Input: 
        net: The pre-initalized and pre-trained YOLO object detection.
        frame: The image you want to detect objects.
        confidence: The minimum confidence to filter out the weak entity predictions.
        output_layer_names: The output layer of YOLO model.
    
    Process: 
        Applying the blob on the image using opencv-dnn and passing it forward through YOLO object detector,
        then, Loop through each output through each detections and filter only peoples,
        with avoiding the weak entity predictions.
    
    Output:
        Return the important inforamtions about the person detections which are 
            1- The bounding boxes.
            2- The confidences.
            3- The centroids.

'''
def extract_detection_informations(frame, net, output_layer_names, confidence):
    height, width = frame.shape[:2]
    


    # Create a blob using opencv-dnn to pass it through the YOLO model.
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    
    '''
    Passing the blob frame to YOLO model,
    Then applying a forward of YOLO object detector.
    '''
    net.setInput(blob)
    layer_outputs = net.forward(output_layer_names)

    boxes = []              # For holding the detected bounding boxes.
    confidences = []        # For holding the cdetected confidences.
    centroids = []          # For holding the detected centroid of objects.

    # Iterate over each of the layer outputs.
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
            if conf > confidence and classID == personIdx:
                
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

