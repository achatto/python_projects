import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('quad.png',1)
cv2.imshow("Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)
ret,_ = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
edges = cv2.Canny(gray,0.66*ret,1.33*ret)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
fig = plt.figure()
im2= img
cv2.drawContours(im2, contours, -1, (0,255,0), 3)
plt.subplot(121),plt.imshow(img, 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(im2, 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.draw()
plt.waitforbuttonpress(0) # this will wait for indefinite time
plt.close(fig)

