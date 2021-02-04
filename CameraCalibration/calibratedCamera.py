import numpy as np 
import cv2
import glob 
import pickle
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

'''
Define object points [Chessboard] to find.
    nx: number of inside corner in x
    ny: number of inside corners in y
'''
nx = 9
ny = 6

# Prepare object points, like (0,0,0) , (5,3,2). (2,1,4)and so on.
object_point = np.zeros((nx*ny, 3), np.float32)
object_point[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1, 2)

object_points = []      # 3d points in real world space.
image_points = []       # 2d points in  image plane.

images = glob.glob('train_images/calibration*.jpg')

for idx, image in enumerate(images):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # Convert to grayscale.
    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)      # Find the corner using opencv chessboard.
    
    # If found corners add object points and image points.
    if ret == True:
        object_points.append(object_point)
        image_points.append(corners)

        cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
        write_name = "output_test/corners_found"+str(idx)+".jpg"
        cv2.imwrite(write_name, img)

#load image for reference to calculate all calibration coefficients for the undistortion process.
img = cv2.imread('train_images/calibration1.jpg')
img_size = (img.shape[1],img.shape[0])

# Do camera calibration given object points and image points
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points, image_points, img_size, None, None)

undistort = cv2.undistort(img, mtx, dist, None, mtx)
cv2.imshow("frame", img)
cv2.imshow("undistort", undistort)

cv2.waitKey(0)
cv2.destroyAllWindows()


