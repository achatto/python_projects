import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('quad.png',1)
cv2.imshow("Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.GaussianBlur(img, (5, 5), 0)
cv2.waitKey(0)

ret,edges = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#edges = cv2.Canny(gray,0.66*ret,1.33*ret)
cv2.imshow("Image", edges)
#gray = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    if cv2.isContourConvex(c):
        l = cv2.arcLength(c, True)
        poly = cv2.approxPolyDP(c, 0.05*l, True)
        if len(poly) == 4:
            im2 = cv2.drawContours(img, [c], -1, (0,255,0), 3)

#im2 = cv2.drawContours(img, contours, 73, (0,255,0), 3)

fig = plt.figure()
plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(im2)
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.draw()
plt.waitforbuttonpress(0) # this will wait for indefinite time
plt.close(fig)
