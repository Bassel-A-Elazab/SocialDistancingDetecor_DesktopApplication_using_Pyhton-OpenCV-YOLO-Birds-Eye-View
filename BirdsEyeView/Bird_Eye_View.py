import cv2
import numpy as np
from scipy.spatial.distance import pdist, squareform

def get_camera_perspective(img, source_points):

    IMAGE_H = img.shape[0]
    IMAGE_W = img.shape[1]

    src = np.float32(np.array(source_points))
    dst = np.float32( [[0, IMAGE_H], [IMAGE_W, IMAGE_H], [0, 0], [IMAGE_W, 0]] )

    M = cv2.getPerspectiveTransform(src, dst)
    M_INV = cv2.getPerspectiveTransform(dst, src)
    
    return M, M_INV


def draw_circle_bird_eye_view(frame, pedestrian_boxes, M, scale_w, scale_h):
    
    color_green = (0, 255, 0)

    node_radius = 10
    color_node = (192, 133, 156)
    thickness_node = 1
    solid_back_color = (41, 41, 41)

    blank_image = np.zeros((int(IMAGE_H ), int(IMAGE_W ), 3), np.uint8)
    blank_image[:] = solid_back_color

    warped_pts = []
    frame_pts = []

    for(i, (prob, bbox, centorid)) in enumerate(pedestrian_boxes):

        (startX, startY, endX, endY) = bbox     # extract the box coordinates.
        (cX, cY) = centorid                     # extract the centroid coordinates.
        pts_detect = np.array([[[cX, cY]]], dtype="float32")
        warped_pt = cv2.perspectiveTransform(pts_detect, M)[0][0]

        warped_pt_scaled = [int(warped_pt[0]), int(warped_pt[1])]
        warped_pts.append(warped_pt_scaled)

        frame_pts.append([startX, startY, endX, endY])

        bird_image = cv2.circle(
            blank_image,
            (warped_pt_scaled[0], warped_pt_scaled[1]),
            node_radius,
            color_node,
            20
        )

        frame = cv2.rectangle(frame, (startX, startY), (endX, endY), color_green, 2)
    return warped_pts, frame_pts, bird_image