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


def draw_lines_between_nodes(warped_points, frame_points, bird_image, frame_image, d_thresh):
    
    color_red = (255, 0, 0)

    p = np.array(warped_points)
    p_frame = np.array(frame_points)

    dist_condensed = pdist(p)
    dist = squareform(dist_condensed)

    # Really close: 6 feet mark
    dd = np.where(dist < d_thresh)
    six_feet_violations = len(np.where(dist_condensed < d_thresh)[0])

    color_6 = (52, 92, 227)
    for i in range(int(np.ceil(len(dd[0]) / 2))):
        if dd[0][i] != dd[1][i]:
            point1 = dd[0][i]
            point2 = dd[1][i]


            startX1 = p_frame[point1][0]
            startY1 = p_frame[point1][1]
            endX1 = p_frame[point1][2]
            endY1 = p_frame[point1][3]

            startX2 = p_frame[point2][0]
            startY2 = p_frame[point2][1]
            endX2 = p_frame[point2][2]
            endY2 = p_frame[point2][3]

            cv2.line(
                bird_image,
                (p[point1][0], p[point1][1]),
                (p[point2][0], p[point2][1]),
                color_6,
                1,
            )
            frame_image = cv2.rectangle(frame_image, (startX1, startY1), (endX1, endY1), color_red, 2)
            frame_image = cv2.rectangle(frame_image, (startX2, startY2), (endX2, endY2), color_red, 2)
    
    return frame_image

