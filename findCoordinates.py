import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import numpy as np
import cv2

image1 = cv2.imread('left1.16mm.jpg')
# image2 = cv2.imread('left2.16mm.jpg')

# gray1 = cv2.cvtColor(image1, COLOR_BGR2GRAY)
# gray2 = cv2.cvtColor(image2, COLOR_BGR2GRAY)
# gray1 = np.float32(gray1)
# gray2 = np.float32(gray2)
#
# corner1 = cv2.goodFeatures


# edge1 = cv2.Canny(image1, 100, 255)
# edge2 = cv2.Canny(image2, 100, 255)


cv2.imshow('Corner', image1)
# print "Hello"4
