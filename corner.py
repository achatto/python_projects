import cv2
import numpy as np

filename = 'check.jpg'

gray_img = cv2.imread(filename)
gray_img = cv2.cvtColor(gray_img,cv2.COLOR_BGR2GRAY)
#gray_img = np.float32(gray_img)
cv2.imshow('Original', gray_img)
cv2.waitKey(0)
corner = cv2.cornerHarris(gray_img, 2, 3, 0.1)
#corner = cv2.goodFeaturesToTrack(gray_img, 25, 0.1,1)
print(corner.dtype)
cv2.imshow('corner',corner)
cv2.waitKey(0)
corner = cv2.dilate(corner, None)
cv2.imshow('dilated',corner)
cv2.waitKey(0)
