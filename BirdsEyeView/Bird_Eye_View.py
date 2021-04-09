import cv2
import numpy as np
from scipy.spatial.distance import pdist, squareform

def get_camera_perspective(img, src_points):
    IMAGE_H = img.shape[0]
    IMAGE_W = img.shape[1]

    src = np.float32(np.array(src_points))
    dst = np.float32( [[0, IMAGE_H], [IMAGE_W, IMAGE_H], [0, 0], [IMAGE_W, 0]] )

    M = cv2.getPerspectiveTransform(src, dst)
    M_INV = cv2.getPerspectiveTransform(dst, src)
    
    return M, M_INV


