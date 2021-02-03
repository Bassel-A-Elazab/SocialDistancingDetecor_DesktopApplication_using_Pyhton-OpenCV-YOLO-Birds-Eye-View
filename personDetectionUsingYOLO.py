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

